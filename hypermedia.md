FORMAT: 1A
HOST: http://localhost:5000/

# JobSeekAPI

This API is a simple seeking job service. The API serves JSON data extended by the [Mason 

hypermedia format](https://github.com/JornWildt/Mason). Custom link relations and resource 

profiles have been included in this API document - they are not resources.

# Group Link Relations

This section described custom link relations defined in this API. Custom link relations are 

CURIEs that use the mumeta prefix. 

## add-job

This is a control that is used to add an job to users who want to find a job. The control 

includes a JSON schema and must be accessed with POST. 

## add-company

This is a control that is used to add a company offering jobs. The control includes a JSON 

schema and must be accessed with POST.

## add-category

This is a control that is used to add a job category. The control includes a JSON schema 

and must be accessed with POST.

## add-region

This is a control that is used to add a region. The control includes a JSON schema and must 

be accessed with POST.

## jobs-all

Leads to the root level jobs collection which is a list of all jobs. This collection can be 

sorted using query parameters as described in the resource documentation.

## jobs-by-company

Leads to a collection resoruce that includes all jobs of the company.

## jobs-by-region

Leads to a collection resoruce that includes all jobs of the region.

## jobs-by-category

Leads to a collection resoruce that includes all jobs of the category.

## companys-all

Leads to the root level companys collection which is a list of all companys known to the 

API. 

## categorys-all

Leads to the root level categories collection which is a list of all categories known to 

the API. 

## regions-all

Leads to the root level regions collection which is a list of all regions known to the API. 

## region-edit

Edit the region. Must be accessed with PUT.

## category-edit

Edit the category. Must be accessed with PUT.

## company-edit

Edit the company. Must be accessed with PUT.

## region-delete

Deletes the associated resource. Must be accessed with DELETE

## category-delete

Deletes the associated resource. Must be accessed with DELETE

## company-delete

Deletes the associated resource. Must be accessed with DELETE

## job-delete

Deletes the associated resource. Must be accessed with DELETE

## job-seeker-delete

The seeker cancel the application of a job. Must be accessed with DELETE

## job-edit

Edit the job. Must be accessed with PUT.

## seeker-edit

Edit the seeker. Must be accessed with PUT.

##seekers-by-job

Leads to the seeker collection which is a list of all seekers applying the job. 

##jobs-by-seeker

Leads to the job collection which is a list of all jobs applied by the seeker. 

##jobs-apply

A seeker want to apply the job. Must be accessed with POST.

# Group Profiles

This section includes resource profiles which provide semantic descriptions for the 

attributes of each resource, as well as the list of controls (by link relation) available 

from that resource.

## Job Profile

Profile definition for all job related resources.

### Link Relations

This section lists all possible link relations associated with jobs; not all of them are 

necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [add-job](reference/link-relations/add-job)
 * [jobs-all](reference/link-relations/jobs-all)
 * [jobs-by-company](reference/link-relations/jobs-by-company)
 * [jobs-by-region](reference/link-relations/jobs-by-region)
 * [jobs-by-category](reference/link-relations/jobs-by-category)
 * [job-edit](reference/link-relations/job-edit)
 * [job-delete](reference/link-relations/job-delete)
 * [jobs-by-seeker](reference/link-relations/jobs-by-seeker)
 * [seekers-by-job](reference/link-relations/seekers-by-job)
 * [job-delete](reference/link-relations/job-delete)
 * [job-seeker-delete](reference/link-relations/job-seeker-delete)
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-

relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `job_name`: A name of a job is mandatory.
 * `description`:Description of a job. Mandatory.
 * `salary`: Salary of a job
 * `number of application`: Number of application. Default is 1.
 * `id_company`:Company ID. Mandatory.
 * `id_category`:Category ID. Mandatory.
 * `id_region`:Region ID. Mandatory.
 
## Company Profile

Profile definition for all company related resources.

### Link Relations

This section lists all possible link relations associated with companies; not all of them 

are necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [add-company](reference/link-relations/add-company)
 * [jobs-by-company](reference/link-relations/jobs-company)
 * [companys-by](reference/link-relations/companys-by)
 * [company-edit](reference/link-relations/company-edit)
 * [company-delete](reference/link-relations/company-delete)
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-

relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `name`: A name of a company is mandatory.
 * `introducation`:Introducation of a company. Mandatory.
 * `address`: Address of a company.
 * `telephone`: Telephone of a company.
 * `logo`: Logo of a company.
 
## Seeker Profile

Profile definition for all seeker related resources.

### Link Relations

This section lists all possible link relations associated with seekers; not all of them are 

necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [jobs-by-seeker](reference/link-relations/jobs-by-seeker)
 * [seekers-by-job](reference/link-relations/seeders-by-job)
 * [seeker-edit](reference/link-relations/seeker-edit) 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-

relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `username`: Username. Mandatory.
 * `password`:Password. Mandatory.
 * `speciality`:Speciality. Mandatory.
 * `address`: Address .
 * `CV`:CV. Mandatory.
 * `identity`:Identity. Mandatory.
 * `telephone`: Telephone of a company.
 * `desired position`:Desired position. Mandatory.
 * `desired region`:Desired region. 
 
 ## Category Profile

Profile definition for all category related resources.

### Link Relations

This section lists all possible link relations associated with categories; not all of them 

are necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [jobs-by-category](reference/link-relations/jobs-by-category)
 * [categorys-all](reference/link-relations/categroys-all)
 * [category-edit](reference/link-relations/category-edit) 
 * [category-delete](reference/link-relations/category-delete) 
 * [add-category](reference/link-relations/add-category) 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-

relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `content`: Category name. Mandatory. 
 
## Region Profile

Profile definition for all region related resources.

### Link Relations

This section lists all possible link relations associated with categories; not all of them 

are necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [jobs-by-region](reference/link-relations/jobs-by-region)
 * [regions-all](reference/link-relations/regions-all)
 * [region-edit](reference/link-relations/region-edit) 
 * [region-delete](reference/link-relations/region-delete) 
 * [add-region](reference/link-relations/add-region) 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-

relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `content`: Region name. Mandatory.
 
## Error Profile

Profile definition for all errors returned by the API. See [Mason error control]

(https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md#property-

name-error) for more information about errors.

+ Attributes

    + resource_url (string, required) - URI of the resource the error was generated from. 
 
# Group Entry

This group contains the entry point of the API

## Entry Point [/api/]

### Get entry point [GET]

Get the API entry point

+ Request

    + Headers
    
            Accept: application/vnd.mason+json
            
+ Response 200 (application/vnd.mason+json)

    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/jobseek/link-relations#"
                    }
                },
                "@controls": {
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/"
                    },
                    "mumeta:companys-all": {
                        "href": "/api/companys/"
                    },
					 "mumeta:categorys-all": {
                        "href": "/api/categorys/"
                    },
					 "mumeta:regions-all": {
                        "href": "/api/regions/"
                    }
                }
            }

# Group Jobs

All of these resources use the [Artist Profile](reference/profiles/artist-profile). In 

error scenarios [Error Profile](reference/profiles/error-profile) is used.

## Job Collection [/api/jobs/]

A list of all jobs known to the API. This collection can be sorted using the sortby query 

parameter. For each job only job name and description are included, more information can be 

found by following the `self` relation of each job. It only supports GET.

### List all jobs [GET]

Get a list of all artists known to the API.

+ Relation: jobs-all
+ Request

    + Headers
    
            Accept: application/vnd.mason+json

+ Response 200 (application/vnd.mason+json)
    
    + Body

            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                },
                "@controls": {
                    "self": {
                        "href": "/api/jobs/"
                    },
                    "mumeta:companys-all": {
                        "href": "/api/companys/",
                        "title": "All companies",
                        "isHrefTemplate": true,
                        "schema": {
                            "type": "object",
                            "required": []
                        }
                    },
					 "mumeta:categorys-all": {
                        "href": "/api/categorys/",
                        "title": "All categories",
                        "isHrefTemplate": true,
                        "schema": {
                            "type": "object",
                            "required": []
                        }
                    },
					 "mumeta:regions-all": {
                        "href": "/api/regions/",
                        "title": "All regions",
                        "isHrefTemplate": true,
                        "schema": {
                            "type": "object",
                            "required": []
                        }
                    },
					"mumeta:jobs-by-company": {
                        "href": "/api/companys/{company}/jobs/",
                        "title": "All jobs of the company"
                    },
					mumeta:jobs-by-category": {
                        "href": "/api/categorys/{category}/jobs/",
                        "title": "All jobs of the category"
                    },
					mumeta:jobs-by-region": {
                        "href": "/api/regions/{region}/jobs/",
                        "title": "All jobs of the region"
                    },
                    "mumeta:add-job": {
                        "href": "/api/jobs/",
                        "title": "Add job",
                        "encoding": "json",
                        "method": "POST",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "job_name": {
                                    "description": "Job name",
                                    "type": "string"
                                },
                                "description": {
                                    "description": "desciption",
                                    "type": "string"
                                },
                                "salary": {
                                    "description": "Salary",
                                    "type": "Float"
                                },
                                "number of application": {
                                    "description": "number of application",
                                    "type": "Integer"
                                },
                                "id_company": {
                                    "description": "Company ID",
                                    "type": "Integer"
                                },
								"id_category": {
                                    "description": "Category ID",
                                    "type": "Integer"
                                },
								"id_region": {
                                    "description": "Region ID",
                                    "type": "Integer"
                                }
                            },
                            "required": ["job_name", 

"description","salary","id_company","id_category","id_region"]
                        }
                    }
                },
                "items": [
                    {
                        "id_job":"1",
						"job_name": "programmer",
                        "description":"Python",
                        "salary":"3000",
                        "number of application":"3",
                        "id_company": "1",
						"id_category": "1",
						"id_region": "1",
                        "@controls": {
                            "self": {
                                "href": "/api/jobs/1/"
                            }, 
                            "profile": {
                                "href": "/profiles/jobs/"
                            }
                        }
                    }
                ]
            }

### Add job [POST]

Adds a new artist. The artist representation must be valid against the album schema.

+ Relation: add-job
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                 "id_job":"1",
				 "job_name": "programmer",
                 "description":"Python",
                 "salary":"3000",
                  "number of application":"3",
                  "id_company": "1",
				  "id_category": "1",
				  "id_region": "1"
            }

+ Response 201

    + Headers
    
            Location: /api/jobs/1/

+ Response 404 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/jobs/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "'release' is a required property                        
                        Failed validating 'required' in schema:
                        {'properties': {'job_name': {'description': 'name of job',
                        'type': 'string'},
                        'description': {'description': "job description",
                        'type': 'string'},
                        'salary': {'description': 'Salary',                        
                        'type': 'float'},
                        'number of application': {'description': 'number of application',
                        'type': 'Integer'},
                        'id_company': {'description': 'Company ID',
                        'type': 'Integer'},
						'id_category': {'description': 'Category 

ID',
                        'type': 'Integer'},
						'id_region': {'description': 'Rgion ID',
                        'type': 'Integer'}},
                        'required':["job_name", 

"description","salary","id_company","id_category","id_region"],
                        'type': 'object'}
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 415 (application/vnd.mason+json)

    The client did not use the proper content type, or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/jobs/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            } 

## Artist [/api/jobs/{id_job}/]

This resource represents an aritst by a artist name, as identified by the artist's unique 

name. 

+ Parameters

    + id_job: 1 (integer) - job ID(id_job)



### Job information [GET]

Get the job representation.

+ Relation: self
+ Request

    + Headers
    
            Accept: application/vnd.mason+json
        
+ Response 200 (application/vnd.mason+json)

    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/jobseek/link-relations#"
                    }
                },
				"id_job":"1",
				"job_name": "programmer",
                "description":"Python",
                "salary":"3000",
                 "number of application":"3",
                 "id_company": "1",
				 "id_category": "1",
				 "id_region": "1",               
                "@controls": {
                    "mumeta:seekers-by-job": {
                        "href": "/api/jobs/1/seekers/"
                    },
                    "self": {
                        "href": "/api/jobs/1/"
                    },
                    "profile": {
                        "href": "/profiles/job/"
                    },
                    "collection": {
                        "href": "/api/jobs/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All artists"
                    },
					"mumeta:jobs-by-company": {
                        "href": "/api/companys/{company}/jobs/",
                        "title": "All jobs of the company"
                    },
					mumeta:jobs-by-category": {
                        "href": "/api/categorys/{category}/jobs/",
                        "title": "All jobs of the category"
                    },
					mumeta:jobs-by-region": {
                        "href": "/api/regions/{region}/jobs/",
                        "title": "All jobs of the region"
                    },
                    "job-edit": {
                        "href": "/api/jobs/{job}/",
                        "title": "Edit this artist",
                        "encoding": "json",
                        "method": "PUT",
						 "schema": {
                            "type": "object",
                            "properties": {
                                "job_name": {
                                    "description": "Job name",
                                    "type": "string"
                                },
                                "description": {
                                    "description": "desciption",
                                    "type": "string"
                                },
                                "salary": {
                                    "description": "Salary",
                                    "type": "Float"
                                },
                                "number of application": {
                                    "description": "number of application",
                                    "type": "Integer"
                                },
                                "id_company": {
                                    "description": "Company ID",
                                    "type": "Integer"
                                },
								"id_category": {
                                    "description": "Category ID",
                                    "type": "Integer"
                                },
								"id_region": {
                                    "description": "Region ID",
                                    "type": "Integer"
                                }
                            },
                            "required": ["job_name", 

"description","salary","id_company","id_category","id_region"]
                        }                      
                    },
                    "mumeta:job-delete": {
                        "href": "/api/jobs/{job}/",
                        "title": "Delete this job",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an artist that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/",
                "@error": {
                    "@message": "Artist not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit artist information [PUT]

Replace the artist's representation with a new one. Missing optinal fields will be set to 

null. Must validate against the album schema. 

+ Relation: edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "name": "Scandal",
                "unique_name": "scandal",
                "formed": "2009-10-21",
                "disbanded": "2010-11-12",
                "location": "Pop Rock"
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "Release date must be written in ISO format (YYYY-MM-DD)"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an album that doesn't exist (due to non-existent artist or 

album). 

    + Body
    
            {
                "resource_url": "/api/artists/scandal/",
                "@error": {
                    "@message": "Artist not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/scandal/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

### Delete album [DELETE]

Deletes the artist, and all associated albums.

+ Relation: delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an album that doesn't exist (due to non-existent artist 

or album). 

    + Body
    
            {
                "resource_url": "/api/artists/scandal/",
                "@error": {
                    "@message": "Artist not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

# Group Albums

All of these resources use the [Album Profile](reference/profiles/album-profile). In error 

scenarios [Error Profile](reference/profiles/error-profile) is used.

## Album Collection [/api/albums/?sortby={field}]

A list of all albums known to the API. This collection can be sorted using the sortby query 

parameter. For each album only artist name and title is included, more information can be 

found by following the `self` relation of each album. Albums cannot be directly added to 

this collection, it only supports GET.

+ Parameters

    + field (string, optional) - Field to use for sorting
    
        + Default: `title`
        + Members
        
            + `artist`
            + `title`
            + `genre`
            + `release`

### List all albums [GET]

Get a list of all albums known to the API.

+ Relation: albums-all
+ Request

    + Headers
    
            Accept: application/vnd.mason+json

+ Response 200 (application/vnd.mason+json)
    
    + Body

            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                },
                "@controls": {
                    "self": {
                        "href": "/api/albums/"
                    },
                    "mumeta:artists-all": {
                        "href": "/api/artists/",
                        "title": "All artists"
                    },
                    "mumeta:albums-va": {
                        "href": "/api/artists/VA/albums/",
                        "title": "All VA albums"
                    }
                },
                "items": [
                    {
                        "title": "Hello World",
                        "artist": "Scandal",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/scandal/Hello World/"
                            }, 
                            "profile": {
                                "href": "/profiles/album/"
                            }
                        },
                    }, 
                    {
                        "title": "Thorns vs Emperor",
                        "artist": "VA",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/VA/Thorns vs Emperor/"
                            },
                            "profile": {
                                "href": "/profiles/album/"
                            }
                        }
                    }
                ]
            }
        
## Albums by Artist [/api/artists/{artist}/albums/]

This is an album collection by given artist using the artist's unique name. For each album 

only artist and title is included, more information can be found by following the `self` 

relation of each album. Albums released by this artist can be added to this collection.

+ Parameters

    + artist: scandal (string) - artist's unique name (unique_name)

### List albums by artist [GET]

Get a list of albums by an artist.

+ Relation: albums-by
+ Request

    + Headers
    
            Accept: application/vnd.mason+json
    
+ Response 200 (application/vnd.mason+json)

    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                }, 
                "@controls": {
                    "self": {
                        "href": "/api/artists/scandal/albums/"
                    },
                    "mumeta:artists-all": {
                        "href": "/api/artists/",
                        "title": "All artists"
                    },                    
                    "mumeta:albums-all": {
                        "href": "/api/albums/?{sortby}",
                        "title": "All albums",
                        "isHrefTemplate": true,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "sortby": {
                                    "description": "Field to use for sorting",
                                    "type": "string",
                                    "default": "title",
                                    "enum": ["artist", "title", "genre", "release"]
                                }
                            },
                            "required": []
                        }
                    },                    
                    "author": {
                        "href": "/api/artists/scandal/"
                    },
                    "mumeta:add-album": {
                        "href": "/api/artists/scandal/albums/",
                        "title": "Add a new album for this artist",
                        "encoding": "json",
                        "method": "POST",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Album title",
                                    "type": "string"
                                },
                                "release": {
                                    "description": "Release date",
                                    "type": "string",
                                    "pattern": "^[0-9]{4}-[01][0-9]-[0-3][0-9]$"
                                },
                                "genre": {
                                    "description": "Album's genre(s)",
                                    "type": "string"
                                },
                                "discs": {
                                    "description": "Number of discs",
                                    "type": "integer",
                                    "default": 1
                                }
                            },
                            "required": ["title", "release"]
                        }
                    }
                },
                "items": [
                    {
                        "title": "Hello World",
                        "artist": "Scandal",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/scandal/albums/Hello World/"
                            },
                            "profile": {
                                "href": "/profiles/album/"
                            }
                        }
                    }
                ]
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to retrieve list of albums for an artist that doesn't exist.

    + Body
    
            
            {
                "resource_url": "/api/artists/hemuli/albums/",
                "@error": {
                    "@message": "Artist not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Add album for artist [POST]

Adds a new album for the artist. The album representation must be valid against the album 

schema.

+ Relation: add-album
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "Best Scandal",
                "release": "2009-10-21",
                "genre": "Pop Rock",
                "discs": 1
            }

+ Response 201

    + Headers
    
            Location: /api/artists/scandal/albums/Best Scandal/

+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "'release' is a required property
                        
                        Failed validating 'required' in schema:
                        {'properties': {'discs': {'default': 1,
                        'description': 'Number of discs',
                        'type': 'integer'},
                        'genre': {'description': \"Album's genre(s)\",
                        'type': 'string'},
                        'release': {'description': 'Release date',
                        'pattern': '^[0-9]{4}-[01][0-9]-[0-3][0-9]$',
                        'type': 'string'},
                        'title': {'description': 'Album title',
                        'type': 'string'}},
                        'required': ['title', 'release'],
                        'type': 'object'}
                        
                        On instance:
                        {'title': 'Best Scandal'}"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to add an album for an artist that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/hemuli/albums/",
                "@error": {
                    "@message": "Artist not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 409 (application/vnd.mason+json)

    The client is trying to add an album with a title that's already used by another album 

for the same artist.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/",
                "@error": {
                    "@message": "Already exists",
                    "@messages": [
                        "Artist 'scandal' already has album with title 'Hello World'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client did not use the proper content type, or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/artists/scandal/albums/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

## Albums by Various Artists [/api/artists/VA/albums/]

This is an album collection of collaborative releases aka various artists (VA) albums. For 

each album only artist and title is included, and artist is listed as "VA". More 

information can be found by following the `self` relation of each album. VA albums can be 

added to this collection.

### List albums by various artists [GET]

Gets the list of VA albums known to the API.

+ Relation: albums-va
+ Request

    + Headers
    
            Accept: application/vnd.mason+json
        
+ Response 200 (application/vnd.mason+json)

    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                },
                "@controls": {
                    "self": {
                        "href": "/api/artists/VA/albums/"
                    },
                    "mumeta:artists-all": {
                        "href": "/api/artists/",
                        "title": "All artists"
                    },
                    "mumeta:albums-all": {
                        "href": "/api/albums/?{sortby}",
                        "title": "All albums",
                        "isHrefTemplate": true,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "sortby": {
                                    "description": "Field to use for sorting",
                                    "type": "string",
                                    "default": "title",
                                    "enum": ["artist", "title", "genre", "release"]
                                }
                            },
                            "required": []
                        }
                    },                    
                    "mumeta:add-album": {
                        "href": "/api/artists/VA/albums/",
                        "title": "Add a new VA album",
                        "encoding": "json",
                        "method": "POST",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Album title",
                                    "type": "string"
                                },
                                "release": {
                                    "description": "Release date",
                                    "type": "string",
                                    "pattern": "^[0-9]{4}-[01][0-9]-[0-3][0-9]$"
                                },
                                "genre": {
                                    "description": "Album's genre(s)",
                                    "type": "string"
                                },
                                "discs": {
                                    "description": "Number of discs",
                                    "type": "integer",
                                    "default": 1
                                }
                            },
                            "required": ["title", "release"]
                        }
                    }
                },
                "items": [
                    {
                        "title": "Thorns vs Emperor",
                        "artist": "VA",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/VA/albums/Thorns vs Emperor/"
                            },
                            "profile": {
                                "href": "/profiles/album/"
                            }
                        }
                    }
                ]
            }

### Add new various artists album [POST]

Adds a new VA album. The album representation must be valid against the album schema.

+ Relation: add-album
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "Transcendental",
                "release": "2015-10-23",
                "genre": "Post-Rock, Atmospheric Sludge Metal",
                "discs": 1
            }

+ Response 201

    + Headers
    
            Location: /api/artists/VA/albums/Transcendental/

+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "Release date must be written in ISO format (YYYY-MM-DD)"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 409 (application/vnd.mason+json)

    The client is trying to add an album with a title that already exists.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/",
                "@error": {
                    "@message": "Already exists",
                    "@messages": [
                        "Artist 'VA' already has album with title 'Thorns vs Emperor'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/scandal/albums/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

## Album [/api/artists/{artist}/albums/{title}/]

This resource represents an album by a single artist, as identified by the artist's unique 

name and the albm's title. It includes the list of tracks on the album in addition to the 

album's own metadata. Individual tracks are usually only visited when modifying their data. 

They use the [Track Profile](/reference/profiles/track-profile).

+ Parameters

    + artist: scandal (string) - artist's unique name (unique_name)
    + title: Hello World (string) - album's title


### Album information [GET]

Get the album representation.

+ Relation: self
+ Request

    + Headers
    
            Accept: application/vnd.mason+json
        
+ Response 200 (application/vnd.mason+json)

    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                },
                "title": "Hello World",
                "release": "2014-12-03",
                "genre": "Pop Rock",
                "discs": 1,
                "artist": "Scandal",
                "@controls": {
                    "author": {
                        "href": "/api/artists/scandal/"
                    },
                    "mumeta:albums-by": {
                        "href": "/api/artists/scandal/albums/"
                    },
                    "self": {
                        "href": "/api/artists/scandal/albums/Hello World/"
                    },
                    "profile": {
                        "href": "/profiles/album/"
                    },
                    "collection": {
                        "href": "/api/albums/"
                    },
                    "mumeta:artists-all": {
                        "href": "/api/artists/",
                        "title": "All artists"
                    },
                    "mumeta:add-track": {
                        "href": "/api/artists/scandal/albums/Hello World/",
                        "title": "Add a track to this album",
                        "encoding": "json",
                        "method": "POST",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Track title",
                                    "type": "string"
                                },
                                "disc_number": {
                                    "description": "Disc number",
                                    "type": "integer",
                                    "default": 1
                                },
                                "track_number": {
                                    "description": "Track number on disc",
                                    "type": "integer"
                                },
                                "length": {
                                    "description": "Track length",
                                    "type": "string",
                                    "pattern": "^:[0-9]{2}:[0-5][0-9]:[0-5][0-9]$"
                                }
                            },
                            "required": ["title", "track_number", "length"]
                        }
                    },
                    "edit": {
                        "href": "/api/artists/scandal/albums/Hello World/",
                        "title": "Edit this album",
                        "encoding": "json",
                        "method": "PUT",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Album title",
                                    "type": "string"
                                },
                                "release": {
                                    "description": "Release date",
                                    "type": "string",
                                    "pattern": "^[0-9]{4}-[01][0-9]-[0-3][0-9]$"
                                },
                                "genre": {
                                    "description": "Album's genre(s)",
                                    "type": "string"
                                },
                                "discs": {
                                    "description": "Number of discs",
                                    "type": "integer",
                                    "default": 1
                                }
                            },
                            "required": ["title", "release"]
                        }
                    },
                    "mumeta:delete": {
                        "href": "/api/artists/scandal/albums/Hello World/",
                        "title": "Delete this album",
                        "method": "DELETE"
                    }
                },
                "items": [
                    {
                        "title": "Image",
                        "length": "00:04:26",
                        "disc_number": 1,
                        "track_number": 1,
                        "@controls": {
                            "self": {
                                "href": "/api/artists/scandal/albums/Hello World/1/1/"
                            },
                            "profile": {
                                "href": "/profiles/track/"
                            }
                        }
                    }
                ]
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an album that doesn't exist (either due to non-existent 

artist or album).

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Yellow/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
### Add track to album [POST]

Adds a new track to the album. The track representation must be valid against the track 

schema. Also its position on the album (combination of disc number and track number) must 

be unoccupied.

+ Relation: add-track
+ Request (application/json)

    + Headers
    
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "Your Song",
                "disc_number": 1,
                "track_number": 2,
                "length": "00:03:43"
            }

+ Response 201

    + Headers
    
            Location: /api/artists/scandal/albums/Hello World/1/2/
            
    + Body
    
            {}
            


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Hello World/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [
                        "'3:43' does not match '^[0-9]{2}:[0-5][0-9]:[0-5][0-9]$'
                        
                        Failed validating 'pattern' in schema['properties']['length']:
                        {'description': 'Track length',
                        'pattern': '^[0-9]{2}:[0-5][0-9]:[0-5][0-9]$',
                        'type': 'string'}
                        
                        On instance
                        ['length']: '3:43'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to add a track to an album that doesn't exist (due to non-existent 

artist or album).

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Yellow/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 409 (application/vnd.mason+json)

    The client is trying to add a track with a combination of disc and track numbers that 

is already occupied.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Hello World/",
                "@error": {
                    "@message": "Already exists",
                    "@messages": [
                        "Album 'Hello World' already has a track at 1.1"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

            
+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/scandal/albums/Hello World/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

### Edit album information [PUT]

Replace the album's representation with a new one. Missing optinal fields will be set to 

null. Must validate against the album schema. 

+ Relation: edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "Hello World",
                "release": "2014-12-03",
                "genre": "Pop Rock, Power Pop",
                "discs": 1
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Hello World/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "Release date must be written in ISO format (YYYY-MM-DD)"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an album that doesn't exist (due to non-existent artist or 

album). 

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Yellow/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
+ Response 409 (application/vnd.mason+json)

    The client is trying to change the album's title to a one that is already in use for 

the artist.

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Honey/",
                "@error": {
                    "@message": "Title reserved",
                    "@messages": [
                        "Artist 'scandal' already has another album with title 'Hello 

World'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
        
+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/scandal/albums/Hello World/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

### Delete album [DELETE]

Deletes the album, and all associated tracks.

+ Relation: delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an album that doesn't exist (due to non-existent artist 

or album). 

    + Body
    
            {
                "resource_url": "/api/artists/scandal/albums/Yellow/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

## Various Artists Album [/api/artists/VA/albums/{title}/]

This resource represents an album by multiple artists, as identified by the album's title. 

It includes the list of tracks on the album in addition to the album's own metadata. 

Individual tracks are usually only visited when modifying their data. They use the [Track 

Profile](/reference/profiles/track-profile).

+ Parameters

    + title: 'Thorns vs Emperor' (string) - album's title


### Album information [GET]

Get the album's representation.

+ Relation: self
+ Request

    + Headers
    
            Accept: application/vnd.mason+json
        
+ Response 200 (application/vnd.mason+json)
 
    + Body
    
            {
                "@namespaces": {
                    "mumeta": {
                        "name": "/musicmeta/link-relations#"
                    }
                },
                "title": "Thorns vs Emperor",
                "release": "1999-01-01",
                "genre": "Black Metal",
                "discs": 1,
                "artist": "VA",
                "@controls": {
                    "mumeta:albums-va": {
                        "href": "/api/artists/VA/albums/",
                        "title": "All VA albums"
                    },
                    "self": {
                        "href": "/api/artists/VA/albums/Thorns vs Emperor/"
                    },
                    "profile": {
                        "href": "/profiles/album/"
                    },
                    "collection": {
                        "href": "/api/albums/"
                    },
                    "mumeta:artists-all": {
                        "href": "/api/artists/",
                        "title": "All artists"
                    },
                    "mumeta:add-track": {
                        "href": "/api/artists/VA/albums/Thorns vs Emperor/",
                        "title": "Add a track to this album",
                        "encoding": "json",
                        "method": "POST",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Track title",
                                    "type": "string"
                                },
                                "disc_number": {
                                    "description": "Disc number",
                                    "type": "integer",
                                    "default": 1
                                },
                                "track_number": {
                                    "description": "Track number on disc",
                                    "type": "integer"
                                },
                                "length": {
                                    "description": "Track length",
                                    "type": "string",
                                    "pattern": "^:[0-9]{2}:[0-5][0-9]:[0-5][0-9]$"
                                },
                                "va_artist": {
                                    "description": "Track artist unique name (mandatory on 

VA albums)",
                                    "type": "string"
                                }
                            },
                            "required": ["title", "track_number", "length", "va_artist"]
                        }
                    },
                    "edit": {
                        "href": "/api/artists/VA/albums/Thorns vs Emperor/",
                        "title": "Edit this album",
                        "encoding": "json",
                        "method": "PUT",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "description": "Album title",
                                    "type": "string"
                                },
                                "release": {
                                    "description": "Release date",
                                    "type": "string",
                                    "pattern": "^[0-9]{4}-[01][0-9]-[0-3][0-9]$"
                                },
                                "genre": {
                                    "description": "Album's genre(s)",
                                    "type": "string"
                                },
                                "discs": {
                                    "description": "Number of discs",
                                    "type": "integer",
                                    "default": 1
                                }
                            },
                            "required": ["title", "release"]
                        }
                    },
                    "mumeta:delete": {
                        "href": "/api/artists/VA/albums/Thorns vs Emperor/",
                        "title": "Delete this album",
                        "method": "DELETE"
                    }
                },
                "items": [
                    {
                        "title": "Exördium",
                        "length": "00:03:00",
                        "disc_number": 1,
                        "track_number": 1,
                        "va_artist": "Emperor",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/VA/albums/Thorns vs Emperor/1/1/"
                            },
                            "profile": {
                                "href": "/profiles/track/"
                            }
                        }
                    },
                    {
                        "title": "Aerie Descent",
                        "length": "00:08:34",
                        "disc_number": 1,
                        "track_number": 2,
                        "va_artist": "Thorns",
                        "@controls": {
                            "self": {
                                "href": "/api/artists/VA/albums/Thorns vs Emperor/1/2/"
                            },
                            "profile": {
                                "href": "/profiles/track/"
                            }
                        }
                    }
                ]
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to get an album that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Transcendental/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

            
### Add track to album [POST]

Adds a new track to the album. The track representation must be valid against the track 

schema. Also its position on the album (combination of disc number and track number) must 

be unoccupied. Note that VA tracks have the additional required field `va_artist` which 

indicates the track's author.

+ Relation: add-track
+ Request (application/json)

    + Headers
    
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "I am",
                "disc_number": 1,
                "track_number": 3,
                "length": "00:05:04",
                "va_artist": "emperor"
            }

+ Response 201

    + Headers
    
            Location: /api/artists/VA/albums/Thorns vs Emperor/1/2/


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Thorns vs Emperor/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [
                        "'5:04' does not match '^[0-9]{2}:[0-5][0-9]:[0-5][0-9]$'
                        
                        Failed validating 'pattern' in schema['properties']['length']:
                        {'description': 'Track length',
                        'pattern': '^[0-9]{2}:[0-5][0-9]:[0-5][0-9]$',
                        'type': 'string'}
                        
                        On instance
                        ['length']: '5:04'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to add a track for an album that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Xenogears/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
        
+ Response 409 (application/vnd.mason+json)

    The client is trying to add a track with a combination of disc and track numbers that 

is already occupied.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Thorns vs Emperor/",
                "@error": {
                    "@message": "Already exists",
                    "@messages": [
                        "Album 'Thorns vs Emperor' already has a track at 1.1"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
        
+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/VA/albums/Thorns vs Emperor/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

### Edit album information [PUT]

Replace the album's representation with a new one. Missing optinal fields will be set to 

null. Must validate against the album schema. 

+ Relation: edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "title": "Thorns vs Emperor",
                "release": "1999-01-01",
                "genre": "Industrial Black Metal",
                "discs": 1
            }
        
+ Response 204

+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema, 

or has non-existent release date.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Thorns vs Emperor/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "Release date must be written in ISO format (YYYY-MM-DD)"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to modify an album that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Transcendental/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
+ Response 409 (application/vnd.mason+json)

    The client is trying to change the title to a one that is already in use.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Yogsothery/",
                "@error": {
                    "@message": "Title reserved",
                    "@messages": [
                        "Artist 'VA' already has another album with title 'Thorns vs 

Emperor'"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
        
+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid 

JSON.

    + Body
        
            {
                "resource_url": "/api/artists/VA/albums/Thorns vs Emperor/",
                "@error": {
                    "@message": "Unsupported media type",
                    "@messages": [
                        "Use JSON"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error-profile/"
                    }
                }
            }

### Delete album [DELETE]

+ Relation: delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an album that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/artists/VA/albums/Transcendental/",
                "@error": {
                    "@message": "Album not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
