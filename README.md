# coursera-pg4e

## 5: Natural Language
* hand made gin using: `unnest(string_to_array('Hello world', ' '));`
    * query with `EXPLAIN SELECT id, doc FROM docs WHERE '{learn}' <@ string_to_array(doc, ' ');`
* then use postgres's GIN: `CREATE INDEX gin1 ON docs USING gin(string_to_array(doc, ' ')  array_ops);`
    * query using `SELECT id, doc FROM docs WHERE to_tsquery('english', 'learn') @@ to_tsvector('english', doc);`
* compare GIN vs GIST.


## 6: Python and PostgreSQL
* load book 'pg19337' from Project Gutenberg into DB, and query~

## 7: JSON and PostgreSQL
* Studied JSONB, so PostgreSQL can be used for NoSQL
* create index on JSONB, using `BTREE`, `gin(body)`, and `gin(body jsonb_path_ops)`
* demo: using starwar api (`'https://swapi.py4e.com/api/{obj}/1/'`) and `generate_series(1000,5000)` to show case gin index on key, or key-value pair.
* assignment: simpler version than Starwar spider, and use pokemon API: (`https://pokeapi.co/`) to grab 100 pokemon json and stored in pokeapi table.