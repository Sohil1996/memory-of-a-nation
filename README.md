# ذاكرة وطن · Memory of a Nation — v179

**للمعرفة وطن وللوطن ذاكرة** · *Knowledge has a home… and every nation has a memory.*

An AI cultural librarian for books, characters and Saudi culture and history. Arabic is the default language; English is one tap away.

## Deploy

Static site, no build step. Serve the folder as-is (Vercel, Netlify, GitHub Pages, S3, nginx).

```
index.html      the whole app (HTML, CSS and JS in one file)
img/            images, logos, backgrounds and a few short videos
vercel.json     Vercel config
```

On Vercel: import the repo, framework preset **Other**, no build command, output directory `/`.

## Brand

| Token | Hex | Use |
|---|---|---|
| Deep Library Green | `#0E5B49` | Primary brand, light-mode actions |
| Forest Green | `#174D40` | Hover, deep surfaces |
| Antique Gold | `#B99A55` | Accents, details |
| Soft Gold | `#E2C98D` | Highlights, dark-mode actions |
| Warm Ivory | `#F6F1E7` | Light page background |
| Parchment | `#EDE4D2` | Cards, secondary surfaces |

Arabic type: **Alexandria** (Google Fonts).

### Assets

- `img/logo-ar-light.svg`, `img/logo-ar-dark.svg`, `img/logo-en-light.svg`, `img/logo-en-dark.svg`: full logo; the site picks one by language and theme.
- `img/emblem-gold.png`, `img/emblem-soft.png`: emblem only (assistant avatar, narrow headers).
- `img/favicon.png`
- `img/hero-dark.jpg`, `img/hero-light.jpg`: home hero and sign-in.
- `img/chat-dark.jpg`, `img/chat-light.jpg`: chats, My Library, Favorites and every inner page.

To change a background or logo, replace the file and keep its name.

## Notes

- User data (conversations, favorites, encounters, settings) is stored in the browser's `localStorage`. Keys keep their historical `bayan-` prefix so existing saved data still works; they are never shown to users.
