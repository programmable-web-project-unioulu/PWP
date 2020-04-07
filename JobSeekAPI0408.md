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

## job-seeker

Leads to the collection which is a list of all seekers applying the job or a list of all jobs applied by the seeker.

## job-seeker-add

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
 * [job-seeker-add](reference/link-relations/job-seeker-add)
 
The following[IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

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
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `name`: A name of a company is mandatory.
 * `introducation`:Introducation of a company. Mandatory.
 * `address`: Address of a company.
 * `telephone`: Telephone of a company.
 
## Seeker Profile

Profile definition for all seeker related resources.

### Link Relations

This section lists all possible link relations associated with seekers; not all of them are 

necessarily present on each resource type. The following link relations from the mumeta 

namespace are used:

 * [jobs-by-seeker](reference/link-relations/jobs-by-seeker)
 * [seekers-by-job](reference/link-relations/seeders-by-job)
 * [seeker-edit](reference/link-relations/seeker-edit) 
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

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

This section lists all possible link relations associated with categories; not all of them are necessarily present on each resource type. The following link relations from the mumeta namespace are used:

 * [jobs-by-category](reference/link-relations/jobs-by-category)
 * [categorys-all](reference/link-relations/categroys-all)
 * [category-edit](reference/link-relations/category-edit) 
 * [category-delete](reference/link-relations/category-delete) 
 * [add-category](reference/link-relations/add-category) 
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `content`: Category name. Mandatory. 
 
## Region Profile

Profile definition for all region related resources.

### Link Relations

This section lists all possible link relations associated with regions; not all of them are necessarily present on each resource type. The following link relations from the mumeta namespace are used:

 * [jobs-by-region](reference/link-relations/jobs-by-region)
 * [regions-all](reference/link-relations/regions-all)
 * [region-edit](reference/link-relations/region-edit) 
 * [region-delete](reference/link-relations/region-delete) 
 * [add-region](reference/link-relations/add-region) 
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `content`: Region name. Mandatory.

## JobSeeker Profile

Profile definition for all JobSeeker related resources.

### Link Relations

This section lists all possible link relations associated with JobSeeker; not all of them are necessarily present on each resource type. The following link relations from the mumeta namespace are used:

 * [job-seeker-delete](reference/link-relations/job-seeker-delete)
 * [job-seeker-add](reference/link-relations/job-seeker-add)
 
The following [IANA RFC5988](http://www.iana.org/assignments/link-relations/link-relations.xhtml) link relations are also used:

 * profile
 * self
 
### Semantic Descriptors

#### Data Type Album

 * `id_job`: Job ID. Mandatory.
 * `id_seeker`: Seeker ID. Mandatory.
 
## Error Profile

Profile definition for all errors returned by the API. See [Mason error control](https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md#property-name-error) for more information about errors.

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

All of these resources use the [Job Profile](reference/profiles/Job-profile). In 

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
                        "name": "/jobseek/link-relations#"
                    }
                },
                "@controls": {
                    "self": {
                        "href": "/api/jobs/"
                    },
                    "mumeta:companys-all": {
                        "href": "/api/companys/",
                        "title": "All companies"                    
                    },
		            "mumeta:categorys-all": {
                        "href": "/api/categorys/",
                        "title": "All categories"
                    },
		            "mumeta:regions-all": {
                        "href": "/api/regions/",
                        "title": "All regions"
                    },
		            "mumeta:jobs-by-company": {
                        "href": "/api/companys/1/jobs/",
                        "title": "All jobs of the given company"
                    },
		            "mumeta:jobs-by-category": {
                        "href": "/api/categorys/1/jobs/",
                        "title": "All jobs of the given category"
                    },
		            "mumeta:jobs-by-region": {
                        "href": "/api/regions/1/jobs/",
                        "title": "All jobs of the given region"
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
                            "required":["job_name","description","salary","id_company","id_category","id_region"]
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

## Job [/api/jobs/{job}/]

This resource represents a job by a job ID. 

+ Parameters

    + job: 1 (integer) - job ID(id_job)



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
                        "title": "All jobs"
                    },
		            "mumeta:jobs-by-company": {
                        "href": "/api/companys/1/jobs/",
                        "title": "All jobs of the company"
                    },
		            "mumeta:jobs-by-category": {
                        "href": "/api/categorys/1/jobs/",
                        "title": "All jobs of the category"
                    },
		            "mumeta:jobs-by-region": {
                        "href": "/api/regions/1/jobs/",
                        "title": "All jobs of the region"
                    },
                    "mumeta:job-seeker": {
                        "href": "/api/jobs/1/seekers/1/"
                        "title":"Get the seeker list applying the job"
                    },
                    "mumeta:job-seeker-add": {
                        "href": "/api/jobs/1/seekers/1/",
                        "title": "The job is applied by the seeker",
                        "method": "POST"
                    },
                    "job-edit": {
                        "href": "/api/jobs/1/",
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
			                "required": ["job_name","description","salary","id_company","id_category","id_region"]
                        }                      
                    },
                    "mumeta:job-delete": {
                        "href": "/api/jobs/1/",
                        "title": "Delete this job",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an job that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/jobs/1/",
                "@error": {
                    "@message": "Job not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit job information [PUT]

Replace the job's representation with a new one. Missing optinal fields will be set to null.  

+ Relation: job-edit
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
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/jobs/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "job_name,description,salary,id_company,id_region,id_category are required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an job that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/jobs/1/",
                "@error": {
                    "@message": "Job not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/jobs/1/",
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

### Delete job [DELETE]

Deletes the job, and all associated application.

+ Relation: job-delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an job that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/jobs/1/",
                "@error": {
                    "@message": "Job not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
## JobsByCompany [/api/comanys/{company}/jobs/]

A list of all jobs of the given company. For each job only job name and description are included, more information can be found by following the `self` relation of each job. 

+ Parameters

    + company: id_company - Company ID

### List all jobs of the company [GET]

Get a list of all jobs of the given company.

+ Relation: jobs-by-company
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
                    "self": {
                        "href": "/api/company/1/jobs/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
                    "mumeta:company": {
                        "href": "/api/companys/1/",
                        "title": "Get the company"
                    },
                    "mumeta:add-job": {
                        "href": "/api/companys/1/jobs/",
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
                            "required":["job_name","description","salary","id_company","id_category","id_region"]
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

+ Response 404 (application/vnd.mason+json)

    The client is trying to retrieve list of jobs for an company that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/companys/1/jobs/",
                "@error": {
                    "@message": "Company not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Add job [POST]
Adds a new job of the given company. The job representation must be valid.

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

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/companys/1/jobs/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "Failed validating 'required' in schema:
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
			            'id_category': {'description': 'Category ID',
                        'type': 'Integer'},
			            'id_region': {'description': 'Rgion ID',
                        'type': 'Integer'}},
                        'required':['job_name','description','salary','id_company','id_category','id_region'],
                        'type': 'object'}"
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
                "resource_url": "/api/companys/1/jobs/",
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
## JobsByCategory [/api/categorys/{category}/jobs/]

A list of all jobs of the given category. For each job only job name and description are included, more information can be found by following the `self` relation of each job. 

+ Parameters

    + category: id_category - Category ID

### List all jobs of the category [GET]

Get a list of all jobs of the given category.

+ Relation: jobs-by-category
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
                    "self": {
                        "href": "/api/category/1/jobs/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
                    "mumeta:category": {
                        "href": "/api/category/1/",
                        "title": "Get the category"
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

+ Response 404 (application/vnd.mason+json)

    The client is trying to retrieve list of jobs for an category that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/category/1/jobs/",
                "@error": {
                    "@message": "Category not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

## JobsByRegion [/api/regions/{region}/jobs/]

A list of all jobs of the given region. For each job only job name and description are included, more information can be found by following the `self` relation of each job. 

+ Parameters

    + region: id_region - Region ID

### List all jobs of the region [GET]

Get a list of all jobs of the given region.

+ Relation: jobs-by-region
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
                    "self": {
                        "href": "/api/region/1/jobs/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
                    "mumeta:region": {
                        "href": "/api/region/1/",
                        "title": "Get the region"
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

+ Response 404 (application/vnd.mason+json)

    The client is trying to retrieve list of jobs for an region that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/region/1/jobs/",
                "@error": {
                    "@message": "Category not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

# Group Company

All of these resources use the [Company Profile](reference/profiles/company-profile). In error
scenarios [Error Profile](reference/profiles/error-profile) is used.

## Company Collection [/api/companys/]

A list of all companys known to the API. For each company only company name is included, more information can be found by following the `self` relation of each company. 

### List all companies [GET]

Get a list of all albums known to the API.

+ Relation: companys-all
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
                    "self": {
                        "href": "/api/companys/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    }
                },
                "items": [
                    {
                        "name": "Apple",
                        "introduction": "A famous company",
                        "address": "America",
                        "telephone":"1000001",
                        "@controls": {
                            "self": {
                                "href": "/api/companys/1/"
                            }, 
                            "profile": {
                                "href": "/profiles/company/"
                            }
                        }
                    }
                ]
            }

### Add comany [POST]
Adds a new company. The company representation must be valid.

+ Relation: add-company
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                  "name": "Apple",
                  "introduction": "A famous company",
                  "address": "America",
                  "telephone":"1000001"
            }

+ Response 201

    + Headers
    
            Location: /api/companys/1/

+ Response 404 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/companys/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "Failed validating 'required' in schema:
                        {'properties': {'name': {'description': 'name of company',
                        'type': 'string'},
                        'introduction': {'description': "company introduction",
                        'type': 'string'},
                        'address': {'description': 'company address',             
                        'type': 'string'},
                        'telephone': {'description': 'company telephone',
                        'type': 'string'}},
                        'required':['name','introduction','address','telephone'],
                        'type': 'object'}"
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
                "resource_url": "/api/companys/",
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

## Company [/api/companys/{company}/]

This resource represents a company by a company ID. 

+ Parameters

    + company: 1 (integer) - company ID(id_company)

### Company information [GET]

Get the company representation.

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
		        "id_company":"1",
		        "name": "Apple",
                "introduction":"A famous company",
                "address":"America",
                "telephone":"1000001",
                "@controls": {
                    "self": {
                        "href": "/api/companys/1/"
                    },
                    "profile": {
                        "href": "/profiles/company/"
                    },
                    "collection": {
                        "href": "/api/companys/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
		            "mumeta:jobs-by-company": {
                        "href": "/api/companys/1/jobs/",
                        "title": "All jobs of the company"
                    },
                    "company-edit": {
                        "href": "/api/companys/1/",
                        "title": "Edit this company",
                        "encoding": "json",
                        "method": "PUT",
			            "schema": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "description": "Company name",
                                    "type": "string"
                                },
                                "introdution": {
                                    "description": "Company introduction",
                                    "type": "string"
                                },
                                "address": {
                                    "description": "Company address",
                                    "type": "string"
                                },
                                "telephone": {
                                    "description": "Company telephone",
                                    "type": "string"
                                }
                            },
			                "required": ["name","introduction","address","telephone"]
                        }                      
                    },
                    "mumeta:company-delete": {
                        "href": "/api/companys/1/",
                        "title": "Delete this company",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an company that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/companys/1/",
                "@error": {
                    "@message": "company not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit company information [PUT]

Replace the company representation with a new one. Missing optinal fields will be set to null.  

+ Relation: company-edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "name": "Apple",
                "introduction": "A famous company",
                "address": "America",
                "telephone":"1000001"
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/companys/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "name,introduction,address,telephone are required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an job that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/companys/1/",
                "@error": {
                    "@message": "company not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/companys/1/",
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

### Delete company [DELETE]

Deletes the company, and all associated application.

+ Relation: company-delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an company that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/companys/1/",
                "@error": {
                    "@message": "Company not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

# Group Category

All of these resources use the [Category Profile](reference/profiles/category-profile). In error scenarios [Error Profile](reference/profiles/error-profile) is used.

## Category Collection [/api/categorys/]

A list of all categorys known to the API. For each category only category name is included, more information can be found by following the `self` relation of each category. 

### List all categories [GET]

Get a list of all categories known to the API.

+ Relation: categorys-all
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
                    "self": {
                        "href": "/api/categorys/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    }
                },
                "items": [
                    {
                        "content": "programmer",
                        "@controls": {
                            "self": {
                                "href": "/api/categorys/1/"
                            }, 
                            "profile": {
                                "href": "/profiles/category/"
                            }
                        }
                    }
                ]
            }

### Add category [POST]
Adds a new category. The category representation must be valid.

+ Relation: add-category
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                  "content": "programmer"
            }

+ Response 201

    + Headers
    
            Location: /api/categorys/1/

+ Response 404 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/categorys/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "Failed validating 'required' in schema:
                        {'properties': {'content': {'description': 'name of category',
                        'type': 'string'}},
                        'required':['content'],
                        'type': 'object'}"
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
                "resource_url": "/api/categorys/",
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

## Category [/api/categorys/{category}/]

This resource represents a company by a category ID. 

+ Parameters

    + category: 1 (integer) - category ID(id_category)

### Category information [GET]

Get the category representation.

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
		        "id_category":"1",
		        "content": "programmer",
                "@controls": {
                    "self": {
                        "href": "/api/categorys/1/"
                    },
                    "profile": {
                        "href": "/profiles/category/"
                    },
                    "collection": {
                        "href": "/api/categorys/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
		            "mumeta:jobs-by-category": {
                        "href": "/api/categorys/1/jobs/",
                        "title": "All jobs of the category"
                    },
                    "category-edit": {
                        "href": "/api/categorys/1/",
                        "title": "Edit this category",
                        "encoding": "json",
                        "method": "PUT",
			            "schema": {
                            "type": "object",
                            "properties": {
                                "content": {
                                    "description": "Category name",
                                    "type": "string"
                                }
                            },
			                "required": ["content"]
                        }                      
                    },
                    "mumeta:category-delete": {
                        "href": "/api/categorys/1/",
                        "title": "Delete this category",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an category that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/categorys/1/",
                "@error": {
                    "@message": "category not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit category information [PUT]

Replace the category representation with a new one. Missing optinal fields will be set to null.  

+ Relation: category-edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "content": "programmer"
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/categorys/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "content is required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an job that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/categorys/1/",
                "@error": {
                    "@message": "category not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/categorys/1/",
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

### Delete category [DELETE]

Deletes the category, and all associated application.

+ Relation: category-delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an category that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/categorys/1/",
                "@error": {
                    "@message": "Category not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

# Group Region

All of these resources use the [Region Profile](reference/profiles/region-profile). In error scenarios [Error Profile](reference/profiles/error-profile) is used.

## Regions Collection [/api/regions/]

A list of all regions known to the API. For each regions only region name is included, more information can be found by following the `self` relation of each region. 

### List all regions [GET]

Get a list of all regions known to the API.

+ Relation: regions-all
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
                    "self": {
                        "href": "/api/regions/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    }
                },
                "items": [
                    {
                        "content": "OULU",
                        "@controls": {
                            "self": {
                                "href": "/api/regions/1/"
                            }, 
                            "profile": {
                                "href": "/profiles/region/"
                            }
                        }
                    }
                ]
            }

### Add region [POST]
Adds a new region. The region representation must be valid.

+ Relation: add-region
+ Request (application/json)

    + Headers

            Accept: application/vnd.mason+json
        
    + Body
    
            {
                  "content": "OULU"
            }

+ Response 201

    + Headers
    
            Location: /api/regions/1/

+ Response 404 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/regions/",
                "@error": {
                    "@message": "Invalid JSON document",
                    "@messages": [                    
                        "Failed validating 'required' in schema:
                        {'properties': {'content': {'description': 'name of region',
                        'type': 'string'}},
                        'required':['content'],
                        'type': 'object'}"
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
                "resource_url": "/api/regions/",
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

## Region [/api/categorys/{region}/]

This resource represents a region by a region ID. 

+ Parameters

    + region: 1 (integer) - region ID(id_region)

### Region information [GET]

Get the region representation.

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
		        "id_region":"1",
		        "name": "OULU",
                "@controls": {
                    "self": {
                        "href": "/api/regions/1/"
                    },
                    "profile": {
                        "href": "/profiles/region/"
                    },
                    "collection": {
                        "href": "/api/regions/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
		            "mumeta:jobs-by-region": {
                        "href": "/api/regions/1/jobs/",
                        "title": "All jobs of the region"
                    },
                    "region-edit": {
                        "href": "/api/regions/1/",
                        "title": "Edit this region",
                        "encoding": "json",
                        "method": "PUT",
			            "schema": {
                            "type": "object",
                            "properties": {
                                "content": {
                                    "description": "Region name",
                                    "type": "string"
                                }
                            },
			                "required": ["content"]
                        }                      
                    },
                    "mumeta:region-delete": {
                        "href": "/api/regions/1/",
                        "title": "Delete this region",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an region that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/regions/1/",
                "@error": {
                    "@message": "region not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit region information [PUT]

Replace the category representation with a new one. Missing optinal fields will be set to null.  

+ Relation: region-edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "content": "OULU"
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/regions/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "content is required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an region that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/regions/1/",
                "@error": {
                    "@message": "region not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/regions/1/",
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

### Delete region [DELETE]

Deletes the region, and all associated application.

+ Relation: region-delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete an region that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/regions/1/",
                "@error": {
                    "@message": "region not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            
# Group Seeker

All of these resources use the [Seeker Profile](reference/profiles/seeker-profile). In error scenarios [Error Profile](reference/profiles/error-profile) is used.

## Seeker [/api/seekers/{seeker}/]

This resource represents a seeker by a seeker ID. 

+ Parameters

    + seeker: 1 (integer) - seeker ID(id_seeker)

### Seeker information [GET]

Get the seeker representation.

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
		        "id_seeker":"1",
		        "username": "zhangsan",
		        "password": "z123",
		        "speciality": "computer",
		        "address": "OULU",
		        "CV": "computer",
		        "identity": "010198-11A",
		        "telephone": "0400123456",
		        "desired position": "manager",
		        "desired region": "OULU",
                "@controls": {
                    "self": {
                        "href": "/api/seekers/1/"
                    },
                    "profile": {
                        "href": "/profiles/seeker/"
                    },
                    "mumeta:jobs-all": {
                        "href": "/api/jobs/",
                        "title": "All jobs"
                    },
                    "mumeta:companys-all": {
                        "href": "/api/companys/",
                        "title": "All companies"
                    },
		            "mumeta:job-seeker": {
                        "href": "/api/jobs/1/seekers/1/",
                        "title": "All jobs applied by the seeker"
                    },
                    "seeker-edit": {
                        "href": "/api/seekers/1/",
                        "title": "Edit this seeker",
                        "encoding": "json",
                        "method": "PUT",
			            "schema": {
                            "type": "object",
                            "properties": {
                                "uesername": {
                                    "description": "seeker's name",
                                    "type": "string"
                                },
                                "password": {
                                    "description": "seeker's password",
                                    "type": "string"
                                },
                                "speciality": {
                                    "description": "seeker's speciality",
                                    "type": "string"
                                },
                                "address": {
                                    "description": "seeker's address",
                                    "type": "string"
                                },
                                "CV": {
                                    "description": "seeker's CV",
                                    "type": "string"
                                },
                                "telephone": {
                                    "description": "seeker's telephone",
                                    "type": "string"
                                },
                                "desired position": {
                                    "description": "desired postion of the seeker",
                                    "type": "string"
                                },
                                "desired region": {
                                    "description": "desired region of the seeker",
                                    "type": "string"
                                },
                                "identity": {
                                    "description": "seeker's identity",
                                    "type": "string"
                                }
                            },
			                "required": ["username","password","speciality","CV","desired postion","identity"]
                        }                      
                    },
                    "mumeta:category-delete": {
                        "href": "/api/seekers/1/",
                        "title": "Delete this seeker",
                        "method": "DELETE"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an seeker that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/seekers/1/",
                "@error": {
                    "@message": "seekery not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Edit seeker information [PUT]

Replace the seeker representation with a new one. Missing optinal fields will be set to null.  

+ Relation: seeker-edit
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "username": "zhangsan",
		        "password": "z123",
		        "speciality": "computer",
		        "address": "OULU",
		        "CV": "computer",
		        "identity": "010198-11A",
		        "telephone": "0400123456",
		        "desired position": "manager",
		        "desired region": "OULU"
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/seekers/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "username,password,specality,CV,identity,desired postion are required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to edit an seeker that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/seekers/1/",
                "@error": {
                    "@message": "seeker not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/seekers/1/",
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

# Group JobSeeker

All of these resources use the [JobSeeker Profile](reference/profiles/jobseeker-profile). In error scenarios [Error Profile](reference/profiles/error-profile) is used.

## JobSeeker [/api/jobs/{job}/seekers/{seeker}/]

This resource represents a seeker applied a job. 

+ Parameters

    + job: 1 (integer) - job ID(id_job)
    + seeker: 1 (integer) - seeker ID(id_seeker)

### JobSeeker information [GET]

Get the seeker representation.

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
		        "id_seeker":"1",
		        "id_job": "1",
                "@controls": {
                    "self": {
                        "href": "/api/jobs/1/seekers/1/"
                    },
                    "job-seeker-delete": {
                        "href": "/api/jobs/1/seekers/1/",
                        "title": "Delete this application",
                        "method":"DELETE"
                    },
                    "profile": {
                        "href": "/profiles/jobseeker/"
                    },
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
                    },
                    {
                        "id_seeker":"1",
                        "username": "zhangsan",
		                "password": "z123",
		                "speciality": "computer",
		                "address": "OULU",
		                "CV": "computer",
		                "identity": "010198-11A",
		                "telephone": "0400123456",
		                "desired position": "manager",
		                "desired region": "OULU"
                        "@controls": {
                            "self": {
                                "href": "/api/seekers/1/"
                            }, 
                            "profile": {
                                "href": "/profiles/seeker/"
                            }
                        }
                    }
                ]
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to access an seeker that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/jobs/1/seekers/1/",
                "@error": {
                    "@message": "Both job and seeker not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

### Add jobseeker information [POST]

Add the representation that a seeker applied a job. Missing optinal fields will be set to null.  

+ Relation: job-seeker-add
+ Request (application/json)

    + Headers
        
            Accept: application/vnd.mason+json
        
    + Body
    
            {
                "id_job": "1",
		        "id_seeker": "1
            }
        
+ Response 204


+ Response 400 (application/vnd.mason+json)

    The client is trying to send a JSON document that doesn't validate against the schema.

    + Body
    
            {
                "resource_url": "/api/jobs/1/seekers/1/",
                "@error": {
                    "@message": "Invalid date format",
                    "@messages": [
                        "id_job,id_seeker are required"
                    ]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }

+ Response 404 (application/vnd.mason+json)

    The client is trying to add a seeker or a job that doesn't exist. 

    + Body
    
            {
                "resource_url": "/api/jobs/1/seekers/1/",
                "@error": {
                    "@message": "job or seeker not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            

+ Response 415 (application/vnd.mason+json)

    The client sent a request with the wrong content type or the request body was not valid JSON.

    + Body
        
            {
                "resource_url": "/api/jobs/1/seekers/1/",
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

### Delete jobseeker [DELETE]

Deletes the application of the seeker.

+ Relation: job-seeker-delete
+ Request

    + Headers
        
            Accept: application/vnd.mason+json
        
+ Response 204

+ Response 404 (application/vnd.mason+json)

    The client is trying to delete the application that doesn't exist.

    + Body
    
            {
                "resource_url": "/api/jobs/1/seekers/1/",
                "@error": {
                    "@message": "job or seeker not found",
                    "@messages": [null]
                },
                "@controls": {
                    "profile": {
                        "href": "/profiles/error/"
                    }
                }
            }
            


