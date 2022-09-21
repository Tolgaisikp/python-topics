settings = {
  "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_point"
     }
    }
  }
}

body_1km = {
  "query": {
    "bool": {
      "must": {
        "geo_distance": {
          "distance" : "1km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      },
    }
  }
}


body_5km= {
  "query": {
    "bool": {
      "must_not": {
        "geo_distance": {
          "distance" : "1km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      },
      "must": {
        "geo_distance": {
          "distance" : "5km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      }
    }
  }
}

body_30km= {
  "query": {
    "bool": {
      "must_not": {
        "geo_distance": {
          "distance" : "5km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      },
      "must": {
        "geo_distance": {
          "distance" : "30km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      }
    }
  }
}

body_50km= {
  "query": {
    "bool": {
      "must_not": {
        "geo_distance": {
          "distance" : "30km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      },
      "must": {
        "geo_distance": {
          "distance" : "50km",    
          "location": {         
            "lat": 41.0089763,    
            "lon": 28.814482    
          }
        }
      }
    }
  }
}