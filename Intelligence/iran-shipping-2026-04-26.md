# Iran Sanctions Evasion Shipping Watch - 2026-04-26

Source status: 8 live-derived events, 4 fixture-derived events.

## Executive Read

This first vertical slice fuses sanctions, maritime, and conflict indicators into a single normalized event stream. Treat `[MOCK]` items as connector-shape proof, not intelligence claims.

## Events

### OFAC SDN match: BANK MARKAZI JOMHOURI ISLAMI IRAN

- Source: OFAC SDN - https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML
- Timestamp: 2026-04-26T20:11:12.434462+00:00
- Severity: 4
- Actors: BANK MARKAZI JOMHOURI ISLAMI IRAN
- Geo: n/a
- Tags: sanctions, iran, ofac

### OFAC SDN match: BANK MASKAN

- Source: OFAC SDN - https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML
- Timestamp: 2026-04-26T20:11:12.434522+00:00
- Severity: 4
- Actors: BANK MASKAN
- Geo: n/a
- Tags: sanctions, iran, ofac

### OFAC SDN match: BANK REFAH KARGARAN

- Source: OFAC SDN - https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML
- Timestamp: 2026-04-26T20:11:12.434540+00:00
- Severity: 4
- Actors: BANK REFAH KARGARAN
- Geo: n/a
- Tags: sanctions, iran, ofac

### OFAC SDN match: BANK KESHAVARZI IRAN

- Source: OFAC SDN - https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML
- Timestamp: 2026-04-26T20:11:12.434555+00:00
- Severity: 4
- Actors: BANK KESHAVARZI IRAN
- Geo: n/a
- Tags: sanctions, iran, ofac

### Fixture: dark activity risk near Gulf shipping lane [MOCK]

- Source: Windward - https://insights.windward.ai/
- Timestamp: 2026-04-26T12:00:00+00:00
- Severity: 4
- Actors: 422123456
- Geo: Persian Gulf (26.500, 52.000)
- Tags: maritime, sanctions, windward

### DeepStateMap occupied territory feature 1

- Source: DeepStateMap mirror - https://raw.githubusercontent.com/cyterat/deepstate-map-data/main/deepstate-map-data.geojson.gz
- Timestamp: 2026-04-26T20:11:07.195741+00:00
- Severity: 3
- Actors: Russia, Ukraine
- Geo: DeepStateMap occupied-area centroid (45.212, 36.006)
- Tags: conflict, ukraine, map

### DeepStateMap occupied territory feature 2

- Source: DeepStateMap mirror - https://raw.githubusercontent.com/cyterat/deepstate-map-data/main/deepstate-map-data.geojson.gz
- Timestamp: 2026-04-26T20:11:07.197287+00:00
- Severity: 3
- Actors: Russia, Ukraine
- Geo: DeepStateMap occupied-area centroid (45.212, 36.006)
- Tags: conflict, ukraine, map

### Iran Deploys More Mines in the Strait of Hormuz, Sources Say

- Source: UANI blog - https://www.unitedagainstnucleariran.com/news/iran-deploys-more-mines-strait-of-hormuz-sources-say
- Timestamp: 2026-04-24T18:04:11+00:00
- Severity: 3
- Actors: Iran
- Geo: n/a
- Tags: sanctions, iran, uani, shipping

### Trump says Iran having a 'hard time' figuring out who is in charge

- Source: UANI blog - https://www.unitedagainstnucleariran.com/uani_in_news/trump-says-iran-having-hard-time-figuring-out-who-charge
- Timestamp: 2026-04-23T21:24:58+00:00
- Severity: 3
- Actors: Iran
- Geo: n/a
- Tags: sanctions, iran, uani, shipping

### Fixture: Red Sea conflict pressure relevant to shipping risk. [MOCK]

- Source: ACLED - https://acleddata.com/acled-api-documentation
- Timestamp: 2026-04-26T00:00:00+00:00
- Severity: 3
- Actors: Houthi forces, Commercial shipping
- Geo: Red Sea coast (15.369, 44.191)
- Tags: conflict, acled, red-sea

### Fixture: TankerTrackers-style Iran export watch item [MOCK]

- Source: TankerTrackers - https://x.com/TankerTrackers
- Timestamp: 2026-04-26T00:00:00+00:00
- Severity: 3
- Actors: Iran-linked tanker
- Geo: n/a
- Tags: maritime, iran, oil, shipping

### AIS fixture position report for MMSI 422123456 [MOCK]

- Source: AISStream - https://aisstream.io/documentation.html
- Timestamp: 2026-04-26T00:00:00+00:00
- Severity: 2
- Actors: 422123456
- Geo: Fixture vessel (25.270, 55.309)
- Tags: ais, maritime, shipping

## Next Collection Tasks

- Provision Windward credentials and replace fixture alert with official API output.
- Provision AISStream key and run a bounded server-side Persian Gulf sample.
- Provision ACLED credentials and add Yemen/Red Sea filters.
- Decide whether TankerTrackers uses official X API or a licensed archive.
