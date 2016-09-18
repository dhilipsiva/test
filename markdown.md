# The presentation
@k0kubun

## Hello world
- I'm takashi kokubun
- This is a pen

## How are you?
- I'm fine thank you


# image slide
- This is an exampleeee
- You can insert an image

![](/Applications/Keynote.app/Contents/Resources/keynote.help/Contents/Resources/GlobalArt/AppLanding_KeynoteP4.png)


# ActiveRecord::Precount

```rb
Tweet.all.precount(:favorites).each do |tweet|
  p tweet.favorites.count
end
# SELECT `tweets`.* FROM `tweets`
# SELECT COUNT(`favorites`.`tweet_id`), `favorites`.`tweet_id` FROM `favorites` ...
```
