
import validictory


data ={"name": "Alex Conrad", "address": "University Avenue, Palo Alto, CA","zip": "94301", \
 "country": "US",\
 "date-of-birth": "1980-10-18",\
 "gender": "male",\
 "email": "alex@example.com",\
 "phones": {"home": "+1 650-555-1234",\
            "cell": "+1 650-555-4321"}}


schema = {"type": "object"}

schema = {"type": "object",\
 "properties": {"name": {"type": "string"},\
                "address": {"type": "string"},\
                "zip": {"type": "string"},\
                "country": {"type": "string"},\
                "date-of-birth": {"type": "string"},\
                "gender": {"type": "string"},\
                "email": {"type": "string"},\
                "phones": {"type": "object"}}}


schema = {"name": {"type": "string"},\
 "address": {"type": "string"},\
 "zip": {"type": "string", "minLength": 5, "maxLength": 10},\
 "country": {"type": "string", "minLength": 2, "maxLength": 2},\
 "date-of-birth": {"type": "string", "format": "date"},\
 "gender": {"type": "string", "required": "false"},   # Did not work with false\
 "email": {"type": "string", "format": "email"},\
 "phones": {"type": "object"}}




schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "id": "http://jsonschema.net",
  "type": "object",
  "properties": {
    "name": {
      "id": "http://jsonschema.net/name",
      "type": "string"
    },
    "address": {
      "id": "http://jsonschema.net/address",
      "type": "string"
    },
    "zip": {
      "id": "http://jsonschema.net/zip",
      "type": "string"
    },
    "country": {
      "id": "http://jsonschema.net/country",
      "type": "string"
    },
    "date-of-birth": {
      "id": "http://jsonschema.net/date-of-birth",
      "type": "string"
    },
    "gender": {
      "id": "http://jsonschema.net/gender",
      "type": "string"
    },
    "email": {
      "id": "http://jsonschema.net/email",
      "type": "string"
    },
    "phones": {
      "id": "http://jsonschema.net/phones",
      "type": "object",
      "properties": {
        "home": {
          "id": "http://jsonschema.net/phones/home",
          "type": "string"
        },
        "cell": {
          "id": "http://jsonschema.net/phones/cell",
          "type": "string"
        }
      }
    }
  },
  "required": [
    "name",
    "address",
    "zip",
    "country",
    "date-of-birth",
    "gender",
    "email",
    "phones"
  ]
}


schema = {
    "address": {
      "id": "http://jsonschema.net/address",
      "type": "string"
    },
    "zip": {
      "id": "http://jsonschema.net/zip",
      "type": "string"
    },
    "country": {
      "id": "http://jsonschema.net/country",
      "type": "string"
    },
    "date-of-birth": {
      "id": "http://jsonschema.net/date-of-birth",
      "type": "string"
    },
    "gender": {
      "id": "http://jsonschema.net/gender",
      "type": "string"
    },
    "email": {
      "id": "http://jsonschema.net/email",
      "type": "string"
    },
    "phones": {
      "id": "http://jsonschema.net/phones",
      "type": "object",
      "properties": {
        "home": {
          "id": "http://jsonschema.net/phones/home",
          "type": "string"
        },
        "cell": {
          "id": "http://jsonschema.net/phones/cell",
          "type": "string"
        }
      }
    }
  }


validictory.validate(data, schema)            