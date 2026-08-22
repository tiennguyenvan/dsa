Social Media App: expand US to International

1. GEO LATENCY/AVAIL 
   => DB/storage/instances all regions (asian region = zones in asia), CDN
   => Cross data replica (eg: us users comment on asian post)

2. LOCALIZATION 
   => UI translate (lang, txtdir), locale formats (time/num/text)

3. TRAFFIC/DATA GROWTH
   => auto scale, sharding (Asian Users => DB partition 1, ...)

4. COMPLIANCE/CONTENT MODERATION
   => process required data in region if law
   => regional moderation rules
