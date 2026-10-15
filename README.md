<a className="gh-badge" href="https://datahub.io/core/geo-ne-admin1"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

Geodata [data package][datapackage] providing GeoJSON polygons for first-order administrative subdivisions worldwide.


## Data

The data comes from [Natural Earth][natural-earth], a public domain map dataset for cartography and GIS.

The file is the Natural Earth 10m admin-1 GeoJSON with one change: the top-level `crs` member is removed. The build downloads it from the `master` branch of the Natural Earth vector repository on GitHub. That is a development version, not a numbered release, so it can be ahead of the published releases. A GitHub Actions workflow rebuilds the file on the 1st of each month.

[Admin1][doc] is the biggest administrative subdivision of countries. Note that it is very heterogeneous among countries: in the United States 
of America, admin1 represents states, whereas they don't represent inner countries in the United Kingdom. For more information, please see [official documentation][doc] 
or https://en.wikipedia.org/wiki/Table_of_administrative_divisions_by_country.

The `admin1` resource exposes the following key properties:

- **name**: common name for the subdivision.
- **admin**: country name.
- **iso_3166_2**: ISO 3166-2 subdivision code where available.
- **adm0_a3**: ISO 3166-1 alpha-3 country code.

Each feature carries 121 properties in total (names in many languages, codes from other systems, map-label hints); the four above are the main ones. Notes:

- `name` is empty (null) for 7 features.
- `iso_3166_2` is always filled, but 188 values are Natural Earth placeholders rather than real ISO codes (for example `SY-X01~` or `-99-X16~`, used for disputed or special areas). Real ISO codes look like `AR-E`.
- The same `iso_3166_2` code appears on more than one feature in some cases (60 codes).


[natural-earth]: https://www.naturalearthdata.com/
[datapackage]: https://specs.frictionlessdata.io/data-package/
[doc]: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/

## Preparation

To run the script:

```bash
# Install libraries
pip install -r scripts/requirements.txt

# Update the data
python scripts/process.py
```

## License

Natural Earth's [terms of use][ne-terms] put its data in the public domain. They say: "No permission is needed to use Natural Earth. Crediting the authors is unnecessary." Commercial use is allowed. The name translations (`name_*`) come from Wikidata, which Natural Earth says is CC0.

**UNCLEAR: some columns.** We could not establish the licence of the columns below. The data is published as is. Nothing has been removed.

- `type_en`. Natural Earth's own [licensing note][ne-note] (a forum post from December 2009) says some admin-1 columns depend on GADM. It tells users who are worried about licensing to delete them. GADM's [terms][gadm] say: "Redistribution or commercial use is not allowed without prior permission." The post names three columns: the English type, "valid from" and "valid to". This file still has `type_en`. It does not have `valid_from` or `valid_to`. We found no later statement from Natural Earth or GADM that settles this.
- `gn_name`, `woe_label` and `woe_name`. These are text names taken from other databases (GeoNames and Yahoo/Flickr WOE). Natural Earth says the non-geometry attributes are "commonly available facts that are not copyrightable". Nobody has independently confirmed that for these columns. GeoNames publishes its database under CC BY 4.0.
- We did not read the terms for WOE, US NGA GNS or HASC data (the `woe_*`, `gns_*` and `code_hasc` columns). We make no claim about them.

The maintainers offer this package under the [Open Data Commons Public Domain Dedication and License][pddl] (PDDL) 1.0. In plain words, that covers only what the maintainers add, and the parts that Natural Earth places in the public domain. It does not settle the unclear columns above.

All source code is licensed under the [MIT licence][mit].

See [ATTRIBUTION.txt](ATTRIBUTION.txt) for the source credit and the change made to the source data.

[mit]: https://opensource.org/licenses/MIT
[natural-earth]: https://www.naturalearthdata.com/
[pddl]: https://opendatacommons.org/licenses/pddl/1.0/
[ne-terms]: https://www.naturalearthdata.com/about/terms-of-use/
[ne-note]: https://www.naturalearthdata.com/?p=3348
[gadm]: https://gadm.org/license.html
