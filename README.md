<a className="gh-badge" href="https://datahub.io/core/geo-ne-admin1"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

Geodata [data package][datapackage] providing geojson polygons for the largest administrative subdivisions in every countries.


## Data

The data comes from [geoboundaries][geoboundaries], a community effort to make visually pleasing, well-crafted maps with cartography or GIS software at small scale.

[Admin1][doc] is the biggest administrative subdivision of countries. Note that it is very heterogeneous among countries : in the United States 
of America, admin1 represents states, whereas they don't represent the inner countries in the United Kingdom. For more information, please see [official documentation][doc] 
or https://en.wikipedia.org/wiki/Table_of_administrative_divisions_by_country.

The shape of the `admin1` data has the following fields:

* **geometry**:  
  Represents the spatial geometry of the administrative subdivision. It includes:
  - The type of geometry (e.g., `Polygon`, `MultiPolygon`).
  - The associated coordinates that define its boundaries.

* **properties**:  
  Contains metadata describing the administrative subdivision, with the following fields:
  - **name**:  
    The common name for this `admin1` subdivision.
  - **id**:  
    Code for the subdivision inside the country. [Documentation][doc] is not clear what this code is, but it could be FIPS. Note that some countries, like *Vatican*, are so small they don't have inner administrative subdivisions. In such cases, the code could be *null* and is irrelevant.
  - **country**:  
    The name of the country where the subdivision is located.
  - **ISO3166-1-Alpha-3**:  
    The three-letter ISO code of the country.

* **type**:  
  Specifies the type of the feature, typically `Feature` for each administrative subdivision.


[geoboundaries]: https://www.geoboundaries.org/
[datapackage]: http://dataprotocols.org/data-packages/
[doc]: https://www.geoboundaries.org/simplifiedDownloads.html

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

Note that the original data from [geoboundaries][geoboundaries] is public domain. While no credit is 
formally required a link back or credit to [geoboundaries][geoboundaries], [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is much appreciated.

All source code is licenced under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[geoboundaries]: https://www.geoboundaries.org/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[lexman]: http://github.com/lexman
[okfn]: http://okfn.org/
