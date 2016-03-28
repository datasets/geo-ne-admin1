Geodata [data package][datapackage] providing geojson polygons for the largest administrative subdivisions in every countries.


## Data
Note : **this dataset and its source are still in BETA**.

The data comes from [Natural Earth][naturalearth], a community effort to make visually pleasing, well-crafted maps with cartography or GIS software at small scale.

[Admin1][doc] is the biggest administrative subdivision of countries. Note that it is very heterogeneous among countries : in the United States 
of America, admin1 represents states, whereas they don't represent the inner countries in the United Kingdom. For more information, please see [official documentation][doc] 
or https://en.wikipedia.org/wiki/Table_of_administrative_divisions_by_country.

The shape of the admin1 have four fields : 
* name : the common name for this admin1 subdivision
* id : code for the subdivision inside the country. [Documentation][doc] is not clear what this code is, but it could be FIPS. Note that some countries like *Vatican* are so small they don't have inner administrative subdivision. In that case code could be *null* and in any way it is irrelevant.
* country : name of the country
* ISO3166-1-Alpha-3 : three letters iso code of the country

[naturalearth]: http://www.naturalearthdata.com/
[datapackage]: http://dataprotocols.org/data-packages/
[doc]: http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/

## Preparation

To run the script in order to update the data : see [scripts README](scripts/README.md)

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and License][pddl]. 

Note that the original data from [Natural Earth][naturalearth] is public domain. While no credit is 
formally required a link back or credit to [Natural Earth][naturalearth], [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is much appreciated.

All source code is licenced under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[naturalearth]: http://www.naturalearthdata.com/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[lexman]: http://github.com/lexman
[okfn]: http://okfn.org/
