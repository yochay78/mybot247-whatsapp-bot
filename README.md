# MYBOT247 WhatsApp Bot Builder

Build a WhatsApp assistant for your small business in a short conversation with Claude, then open one link to connect your WhatsApp on MYBOT247.

## Use it

Say to Claude that you want a WhatsApp bot for your business, for example "build me a WhatsApp bot for my yoga studio". Claude asks what the business does and your first name, suggests the questions your customers will be asked in WhatsApp, lets you turn questions on or off, reword them or add up to three of your own, and asks who the bot should answer. At the end Claude gives you a link to MYBOT247. The link opens your bot ready to preview, and you create an account and connect your WhatsApp there.

The assistant asks new customers a few short questions and sends you a summary so you can call them back. It does not quote prices or answer open questions. Booking appointments in your Google Calendar is a separate add-on, described on the MYBOT247 page after you open the link.

Supported business types: driving instructors, beauty, personal trainers, yoga and pilates, home repairs, therapy and clinics, private tutors, photography, cleaning, moving, pest control, car services, pet grooming, lawyers, catering, music teachers, air-conditioning technicians, gardening, and any other business.

## Data

The plugin has no connector and makes no network calls. The only thing it produces is a link to https://bot.mybot247.com/start. The link contains the data you chose in the conversation: your first name, the business type and the wording of the bot's questions, encoded in the part of the address after the `#`, which your browser does not send to the server until the page reads it. It contains no WhatsApp login, password, phone number or customer data. Connecting WhatsApp, creating the account and paying happen on MYBOT247, under its own terms and privacy policy at https://mybot247.com.

The script `scripts/make_link.py` runs locally, checks your choices against the list in `references/types.json` and prints the link.

## Support

help@mybot247.com
