<a className="gh-badge" href="https://datahub.io/core/geo-ne-admin1"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

Geodata [data package][datapackage] providing GeoJSON polygons for first-order administrative subdivisions worldwide.


## Data

The data comes from [Natural Earth][natural-earth], a public domain map dataset for cartography and GIS.

[Admin1][doc] is the biggest administrative subdivision of countries. Note that it is very heterogeneous among countries: in the United States 
of America, admin1 represents states, whereas they don't represent inner countries in the United Kingdom. For more information, please see [official documentation][doc] 
or https://en.wikipedia.org/wiki/Table_of_administrative_divisions_by_country.

The `admin1` resource exposes the following key properties:

- **name**: common name for the subdivision.
- **admin**: country name.
- **iso_3166_2**: ISO 3166-2 subdivision code where available.
- **adm0_a3**: ISO 3166-1 alpha-3 country code.


[natural-earth]: https://www.naturalearthdata.com/
[datapackage]: http://dataprotocols.org/data-packages/
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

All data is licensed under the [Open Data Commons Public Domain Dedication and License][pddl]. 

Note that the original data from [Natural Earth][natural-earth] is public domain.

All source code is licenced under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[natural-earth]: https://www.naturalearthdata.com/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
