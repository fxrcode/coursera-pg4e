# coursera-pg4e

## 5: Natural Language
* hand made gin using: `unnest(string_to_array('Hello world', ' '));`
    * query with `EXPLAIN SELECT id, doc FROM docs WHERE '{learn}' <@ string_to_array(doc, ' ');`
* then use postgres's GIN: `CREATE INDEX gin1 ON docs USING gin(string_to_array(doc, ' ')  array_ops);`
    * query using `SELECT id, doc FROM docs WHERE to_tsquery('english', 'learn') @@ to_tsvector('english', doc);`
* compare GIN vs GIST.


## 6: Python and PostgreSQL
* load book 'pg19337' from Project Gutenberg into DB, and query~