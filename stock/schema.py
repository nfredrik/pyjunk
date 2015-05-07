schema = '''{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "id": "/",
  "type": "object",
  "properties": {
    "stocks": {
      "id": "stocks",
      "type": "array",
      "items": {
        "id": "4",
        "type": "object",
        "properties": {
          "dn": {
            "id": "dn",
            "type": "string"
          }
        },
        "additionalProperties": false,
        "required": [
          "dn"
        ]
      },
      "additionalItems": false,
      "required": [
        "4"
      ]
    }
  },
  "additionalProperties": false,
  "required": [
    "stocks"
  ]
}'''