#!/usr/bin/env python3
"""Validate a MYBOT247 bot description and print the link that opens it.

Usage: make_link.py '<json>'     (or pass the JSON on stdin with no argument)
Reads ../references/types.json, which lists the real business types and question ids.
Prints the link on success; prints every problem and exits with 1 otherwise. No network access.
"""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://bot.mybot247.com/start"
FORBIDDEN = ("{{", "}}", "[[", "]]")
MAX_LINK = 6000


def load_types():
    with open(os.path.join(HERE, "..", "references", "types.json"), encoding="utf-8") as f:
        return json.load(f)


def clean(text):
    return " ".join(str(text).split())


def check(data, meta):
    errors = []
    if not isinstance(data, dict):
        return ["the data must be a JSON object"]
    allowed = {"v", "type", "owner", "field", "skip", "extra", "texts", "scope"}
    for key in data:
        if key not in allowed:
            errors.append(f"unknown key {key!r}")
    if data.get("v") != 1:
        errors.append("v must be 1")
    code = data.get("type")
    kind = meta["types"].get(code)
    if not kind:
        errors.append(f"type {code!r} is not one of: {', '.join(meta['types'])}")
        return errors
    owner = clean(data.get("owner") or "")
    if not owner:
        errors.append("owner (the owner's first name) is required")
    elif len(owner) > meta["owner_max"]:
        errors.append(f"owner is longer than {meta['owner_max']} characters")
    elif any(t in owner for t in FORBIDDEN):
        errors.append("owner contains a forbidden character sequence")
    if "field" in kind["setup"]:
        field = clean(data.get("field") or "")
        if len(field) > kind["field_max"]:
            errors.append(f"field is longer than {kind['field_max']} characters")
    elif "field" in data:
        errors.append("field is only used by solo2_general")
    qids = {q["id"] for q in kind["questions"]}
    locked = {q["id"] for q in kind["questions"] if q["locked"]}
    with_options = {q["id"] for q in kind["questions"] if q["options"]}
    skip = data.get("skip")
    if skip is not None:
        if not isinstance(skip, list) or not all(isinstance(s, str) for s in skip):
            errors.append("skip must be a list of question ids")
        else:
            for sid in skip:
                if sid not in qids:
                    errors.append(f"skip: {sid!r} is not a question of {code}")
                elif sid in locked:
                    errors.append(f"skip: {sid!r} must stay on")
            if len(set(skip)) != len(skip):
                errors.append("skip has duplicates")
    extra = data.get("extra")
    if extra is not None:
        if not isinstance(extra, list) or not all(isinstance(s, str) for s in extra):
            errors.append("extra must be a list of strings")
        else:
            if len(extra) > meta["extra_max"]:
                errors.append(f"extra has more than {meta['extra_max']} questions")
            for q in extra:
                errors += check_wording("extra", q, meta)
    texts = data.get("texts")
    if texts is not None:
        if not isinstance(texts, dict):
            errors.append("texts must be an object of question id -> wording")
        else:
            for sid, wording in texts.items():
                if sid not in qids:
                    errors.append(f"texts: {sid!r} is not a question of {code} (the opening message cannot be reworded)")
                elif sid in with_options:
                    errors.append(f"texts: {sid!r} offers numbered options and cannot be reworded here; ask the owner to change it on the page")
                if not isinstance(wording, str):
                    errors.append(f"texts: the wording of {sid!r} must be a string")
                else:
                    errors += check_wording(f"texts.{sid}", wording, meta)
    if data.get("scope") is not None and data["scope"] not in meta["scopes"]:
        errors.append(f"scope must be one of: {', '.join(meta['scopes'])}")
    return errors


def check_wording(where, text, meta):
    out = []
    text = clean(text)
    if not text:
        out.append(f"{where}: empty")
    if len(text) > meta["text_max"]:
        out.append(f"{where}: longer than {meta['text_max']} characters")
    if any(t in text for t in FORBIDDEN):
        out.append(f"{where}: contains {{ }} or [[ ]]")
    return out


def normalize(data):
    out = {"v": 1, "type": data["type"], "owner": clean(data["owner"])}
    if data.get("field"):
        out["field"] = clean(data["field"])
    if data.get("skip") is not None:
        out["skip"] = list(dict.fromkeys(data["skip"]))
    if data.get("extra"):
        out["extra"] = [clean(q) for q in data["extra"]]
    if data.get("texts"):
        out["texts"] = {k: " ".join(v.split()) for k, v in data["texts"].items()}
    if data.get("scope"):
        out["scope"] = data["scope"]
    return out


def link(data):
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    token = base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")
    return f"{BASE}#b={token}"


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    try:
        data = json.loads(text)
    except ValueError as e:
        print(f"PROBLEM: not valid JSON ({e})")
        return 1
    meta = load_types()
    errors = check(data, meta)
    if errors:
        for e in errors:
            print("PROBLEM:", e)
        return 1
    url = link(normalize(data))
    if len(url) > MAX_LINK:
        print(f"PROBLEM: the link is {len(url)} characters, over {MAX_LINK}. Shorten the wording or drop some texts.")
        return 1
    print(url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
