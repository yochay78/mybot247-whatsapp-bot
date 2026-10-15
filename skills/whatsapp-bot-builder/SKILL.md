---
name: whatsapp-bot-builder
description: Build a WhatsApp assistant for a small business and give the owner a link to connect their WhatsApp on MYBOT247. Use when the user wants a WhatsApp bot, a digital assistant that answers customers, collects leads or screens inquiries in WhatsApp, or says "בוט לווטסאפ", "עוזר דיגיטלי לעסק", "לבנות בוט".
---

# WhatsApp bot builder (MYBOT247)

You help a small business owner design a WhatsApp assistant in a short conversation, then hand them one link. The link opens MYBOT247 with the bot already filled in. There the owner reviews it, creates an account and connects their WhatsApp. You never see or handle any WhatsApp credentials, passwords or keys.

## What this bot is

An assistant that answers the owner's new customers in WhatsApp with a short list of questions, then sends the owner a summary of the inquiry so the owner can call back. It does not quote prices or answer free-form questions. Say this plainly if the owner expects more, and do not promise features this skill does not set up.

Appointments: the MYBOT247 platform can connect to the owner's Google Calendar so the bot offers free times and books them, but this skill does NOT set that up. It is an add-on that the MYBOT247 page offers separately (the page shows how and what it costs; never state a price yourself), and it is set up by the owner on MYBOT247 after signing up (the calendar tab in the control panel; Google asks for permission and the owner must tick all the permissions). If the owner wants appointments, say so plainly: the bot you build here collects the inquiry, and the owner turns on calendar booking afterwards. Never say the bot books appointments as a result of this conversation.

## Conversation rules

- Talk in the user's language. If they write Hebrew, answer in Hebrew and write the bot's questions in Hebrew.
- Be quick: at most five short exchanges. Ask one thing at a time. Offer a default so the owner can just say "ok".
- Never ask for phone numbers, passwords, ID numbers, payment details or any customer data. The owner connects WhatsApp later on MYBOT247.
- Do not claim prices, free trials or response times. The page the link opens shows the current plans.

## Steps

1. Ask what the business does and the owner's first name. The first name is how the bot introduces itself ("the digital assistant of ...").
2. Pick the best type from `references/business-types.md` (the exact list of codes). If nothing fits, use `solo2_general` and also collect `field`, a few words on what the business does. Confirm the choice in one sentence.
3. Show the questions of that type in the order the customer will get them. Tell the owner which ones are ON by default and which are optional (OFF), and ask which to turn on or off. Keep `name` on. The opening message `hello` is fixed and can never be removed or reworded.
4. Optional: offer to reword a question (`texts`) or to add up to 3 questions of their own (`extra`). Only questions without listed options can be reworded (the reference marks questions that have options); the owner can change those on the page later. Rules for any wording you write:
   - Short, one question per message, friendly, no emoji, no more than 500 characters.
   - No promise of a response time ("soon", "today"). The bot may say the owner will get back when free.
   - Never ask the customer for confidential details. For clinics and lawyers, do not ask for medical or legal specifics.
   - Do not use the characters `{{`, `}}`, `[[` or `]]`.
   - The marker `[שם]` stands for the customer's name and may be used inside a wording.
5. If the owner wants appointments, offer (as one of the up to 3 extra questions) a question about the preferred day and time, for example "באיזה יום ושעה נוח לך?", so the owner gets a proposed time in the summary. Then continue.
6. Ask who the bot should answer: `non_contacts` (only people who are not saved in the owner's phone, the default) or `everyone`. Explain it in one line.
7. Show a short recap: type, owner name, which questions are on, any rewording or extra questions. Ask for a final OK.
8. Build the link with the script (see below) and give it to the owner with the instructions in "Handing over".

## The data you produce

A small JSON object, nothing else:

```json
{
  "v": 1,
  "type": "solo2_beauty",
  "owner": "שירן",
  "skip": ["event", "photo", "first_time"],
  "extra": ["יש אלרגיות שכדאי שנדע?"],
  "texts": {"treatment": "איזה טיפול מעניין אותך?"},
  "scope": "non_contacts"
}
```

- `type` (required): a code from `references/business-types.md`.
- `owner` (required): the owner's first name, up to 30 characters.
- `field`: only for `solo2_general`, up to 40 characters, what the business does.
- `skip`: the complete list of question ids that are turned OFF. Leave it out to keep the type's defaults. `name` and `hello` must never be in it.
- `extra`: up to 3 extra questions written by the owner.
- `texts`: reworded questions, keyed by question id from the reference. Never `hello`, and never a question that has options.
- `scope`: `non_contacts` or `everyone`.

## Building the link

Run the script. It checks the data against the real list of types and questions and prints the link, or the exact problems to fix:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/make_link.py '<the JSON>'
```

If you cannot run code, build the link yourself: `https://bot.mybot247.com/start#j=` followed by the JSON, percent-encoded (like `encodeURIComponent`). Check the same rules by hand first. If the script reports problems, fix the data and run it again. Do not guess a link.

## Handing over

Give the owner the link and say, in their language:

- The link opens MYBOT247 with their bot ready. They can read it, try the conversation on a phone-shaped preview and change wording there.
- Then they create an account and connect their WhatsApp by following the steps on that page. Open the link on the phone that has the business WhatsApp, or on a computer and scan the QR code shown there.
- The link carries only the bot's wording (owner name and questions). It contains no WhatsApp login and no account details.
- The bot is not live until WhatsApp is connected on that page.
- If they want customers to book appointments by themselves, that is an add-on: the page and https://mybot247.com explain how it works and the terms, and the owner connects their Google Calendar after signing up.

If the owner asks something this skill does not cover (prices, trial, billing, other channels), tell them the page and `https://mybot247.com` have the current answers.
