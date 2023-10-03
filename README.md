# BannerPhraseGenerator
This tool generates my github banner every hour.

## How it works
Simple, it just generates a phrase, places the phrase on a banner template, then pushes it to my github via github api
Then on my droplet on DO, it uses a cron job every hour to use it.
