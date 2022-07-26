# Medium RSS feeds filtered by tag

This repository contains an API to filter [Medium RSS feeds](https://help.medium.com/hc/en-us/articles/214874118-Using-RSS-feeds-of-profiles-publications-and-topics) of user profiles by tag. For instance:

- https://medium-zye5756oia-uc.a.run.app?username=eguidotti&tag=python

This software and its author are in no way affiliated, endorsed, or approved by “Medium” or any of its affiliates.

## Usage

The RSS feed filtered by tag is available at:

```
https://medium-zye5756oia-uc.a.run.app?username=<username>&tag=<tag>
```

| parameter    | description           | example     |
| ------------ | --------------------- | ----------- |
| `<username>` | The Medium @username. | `eguidotti` |
| `<tag>`      | The tag to filter by. | `python`    |

## Hosting

The API is hosted on Google Cloud. 