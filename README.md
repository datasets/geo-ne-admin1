<a className="gh-badge" href="https://datahub.io/core/geo-ne-admin1"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Natural Earth Admin-1 States and Provinces as GeoJSON

GeoJSON polygons for the first-order administrative subdivisions of the world (states, provinces, regions and similar), taken from Natural Earth.

Column definitions and types are in `datapackage.json`.

## Data

`data/admin1.geojson` is one GeoJSON `FeatureCollection`. Each feature is one subdivision, as a `Polygon` or `MultiPolygon`. The properties of each feature are the Natural Earth attributes, unchanged. The main ones are:

| Property | Meaning |
|---|---|
| `name` | Common name of the subdivision, for example `Entre Ríos` |
| `admin` | Name of the country it belongs to, for example `Argentina` |
| `iso_3166_2` | ISO 3166-2 code of the subdivision, for example `AR-E` |
| `adm0_a3` | Country code, for example `ARG`. This is a Natural Earth code. It follows ISO 3166-1 alpha-3, but disputed and special areas have codes of their own, for example `CYN` for Northern Cyprus |
| `iso_a2` | 2-letter country code, for example `AR`. `-1` for disputed and special areas |
| `type`, `type_en` | Kind of subdivision in the local language and in English, for example `Provincia` and `Province` |
| `name_alt`, `name_local` | Alternative name and local-language name, where known |
| `name_en`, `name_fr`, `name_ja` ... | Name translations (from Wikidata). One `name_<language code>` column per language |
| `code_hasc`, `fips`, `postal` | Codes from other systems (HASC, FIPS, postal abbreviation), for example `AR.ER`, `AR08`, `ER` |
| `wikidataid` | Wikidata identifier, for example `Q44762` |
| `gn_id`, `gn_name`, `gns_id`, `gns_name`, `woe_id`, `woe_label`, `woe_name` | Identifiers and names from GeoNames, the US NGA GNS and WOE (Yahoo/Flickr "Where on Earth") |
| `latitude`, `longitude` | A single point for the subdivision, not the polygon |
| `FCLASS_ISO`, `FCLASS_US` ... | Natural Earth feature-class labels, one column per country or standard. See the [Natural Earth documentation][doc] |

The other properties are Natural Earth map-drawing hints (for example `scalerank`, `labelrank`, `min_label`, `max_label`, `mapcolor9`). `datapackage.json` lists only the four main fields (`name`, `admin`, `iso_3166_2`, `adm0_a3`). Every property is in the file.

[Admin-1][doc] is the first level below the country. It is very different from country to country: in the United States of America it is the states, whereas in the United Kingdom it does not represent the inner countries (England, Scotland and so on). For more information, see the [Natural Earth documentation][doc] or the [table of administrative divisions by country][wiki-divisions].

### Known limitations

* `name` is empty (null) for some features. Do not use it as a key.
* `iso_3166_2` is always filled, but some values are Natural Earth placeholders rather than real ISO codes. They are used for disputed or special areas, for example `SY-X01~` or `-99-X16~`. Real ISO codes look like `AR-E`.
* `iso_3166_2` is not unique. Some codes appear on more than one feature, for example a city and the province around it, or several districts that carry the code of their region. Join on it with care.
* `adm0_a3` is not always an ISO code (see the table), and `iso_a2` is `-1` for some disputed and special areas.
* Some properties are empty on many features (for example `name_local`, `region`, `note`).
* The data is the development version of Natural Earth, not a numbered release (see Preparation). The theme is also marked as beta on the Natural Earth download page.
* The licence of a few columns is unclear (see License).

## Data sources

* [Natural Earth][natural-earth], 10m Admin-1 States, Provinces: the polygons and the attributes. Licence: public domain under its [terms of use][ne-terms].
* [Wikidata][wikidata], through Natural Earth: the name translations (`name_*`) and `wikidataid`. Licence: [CC0][cc0], as stated by Natural Earth.
* A few columns come from other databases (GeoNames, WOE, US NGA GNS, HASC; and `type_en`, which Natural Earth's licensing note ties to GADM). Licence: unclear (see [License](#license)).

Changes made to the source data: the file is downloaded from the Natural Earth repository and republished with one change: the top-level `crs` member is removed. All features and properties are otherwise unchanged.

Not endorsed by, or affiliated with, Natural Earth.

[natural-earth]: https://www.naturalearthdata.com/
[ne-terms]: https://www.naturalearthdata.com/about/terms-of-use/
[wikidata]: https://www.wikidata.org/
[cc0]: https://creativecommons.org/publicdomain/zero/1.0/
[doc]: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/
[wiki-divisions]: https://en.wikipedia.org/wiki/Table_of_administrative_divisions_by_country

## Preparation

The script needs Python 3 and the `requests` library. To rebuild `data/admin1.geojson`:

```bash
# Install libraries
pip install -r scripts/requirements.txt

# Update the data
python scripts/process.py
```

The script downloads `ne_10m_admin_1_states_provinces.geojson` from the `master` branch of the [Natural Earth vector repository][ne-vector] on GitHub. That branch is a development version, not a numbered release, so it can be ahead of the published releases.

A GitHub Actions workflow runs the script on the 1st of every month (and on pushes to `main` and on manual runs), and commits `data/admin1.geojson` if it changed.

[ne-vector]: https://github.com/nvkelso/natural-earth-vector

## License

Natural Earth's [terms of use][ne-terms] put its data in the public domain. They say: "No permission is needed to use Natural Earth. Crediting the authors is unnecessary." Commercial use is allowed. The name translations (`name_*`) come from Wikidata, which Natural Earth says is CC0.

**Unclear: some columns.** We could not establish the licence of the columns below. The data is published as is. Nothing has been removed.

* `type_en`. Natural Earth's own [licensing note][ne-note] (a forum post from December 2009) says some admin-1 columns depend on GADM. It tells users who are worried about licensing to delete them. GADM's [terms][gadm] say: "Redistribution or commercial use is not allowed without prior permission." The post names three columns: the English type, "valid from" and "valid to". This file still has `type_en`. It does not have `valid_from` or `valid_to`. We found no later statement from Natural Earth or GADM that settles this.
* `gn_name`, `woe_label` and `woe_name`. These are text names taken from other databases (GeoNames and Yahoo/Flickr WOE). Natural Earth says the non-geometry attributes are "commonly available facts that are not copyrightable". Nobody has independently confirmed that for these columns. GeoNames publishes its database under CC BY 4.0.
* We did not read the terms for WOE, US NGA GNS or HASC data (the `woe_*`, `gns_*` and `code_hasc` columns). We make no claim about them.

The maintainers offer this package under the [Open Data Commons Public Domain Dedication and License][pddl] (PDDL) 1.0. In plain words, that covers only what the maintainers add, and the parts that Natural Earth places in the public domain. It does not settle the unclear columns above.

All source code is licensed under the [MIT licence][mit].

See [ATTRIBUTION.txt](ATTRIBUTION.txt) for the source credit and the change made to the source data.

[mit]: https://opensource.org/licenses/MIT
[pddl]: https://opendatacommons.org/licenses/pddl/1.0/
[ne-note]: https://www.naturalearthdata.com/?p=3348
[gadm]: https://gadm.org/license.html
