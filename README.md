# How To Use?
python main.py

# What it does?
The scripts is intended to perform migration in batches based on dates

# Configuration of SQL
Update your sql in sql.py and place %s for start and end.

# Configuration File
The configuration file contains the configurations to delete the data from the target table.

The configuration file `yaml` should look like this:

```yaml
db_url: <database endpoint>
db_username: <database username>
db_password: <database password>
db_port: <database port>
schema: <schema_name>
start: <start for deletion>
end: <end for deletion>
batch_size: <no of rows>
```
