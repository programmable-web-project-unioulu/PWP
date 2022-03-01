# -------------------- RESTful API ---------------------

# User -----------
class UserCollection(Resource):
    def get(self):
        """
		Docstring
		---
		description: Get the list of manage users
		responses:
			'200':
				description: List of users
				content:
					application/json:
					example:
					- username: test-user-1
					  email_address: test-user-1@oulu.fi
					  password: 1e234d
					  role: BasicUser
					- username: test-user-2
					  email_address: test-user-2@oulu.fi
					  password: 544f8
					  role: Admin
		"""
        pass

    def post(self):
        """
		---
		description: Create a new user
		responses:
			'201':
				description: The user was created successfully
				headers:
				Location:
					description: URI of the new user
					schema:
						type: string
			'400':
				description: username, email_address, password must be string and role must be BasicUser or Admin
			'409':
				description: User already exists
			'415':
				description: Request content type must be JSON
		requestBody:
			description: JSON document that contains basic data for a new user
			content:
				application/json:
					schema:
						$ref: '#/components/schemas/User'
					example:
						username: new-test-user-1
						email_address: new-test-user-1@oulu.fi
						password: e19h63
						role: BasicUser
		"""
        pass


class UserItem(Resource):
    def get(self):
        """
		Docstring
		---
		description: Get details of one user
		parameters:
    	- $ref: '#/components/parameters/username'
		responses:
			'200':
			description: Data of single user
			content:
				application/json:
					examples:
						user-example:
							description: A user that has been created
							value:
								username: test-user-1
								email_address: test-user-1@oulu.fi
								password: 1e234d
								role: BasicUser
			'404':
				description: The user was not found
		"""
        pass

    def put(self):
        """
		Docstring
		---
		description: Update a user by username
		parameters:
    	- $ref: '#/components/parameters/username'
		responses:
			'204':
				description: The user has been deleted
			'404':
				description: The user was not found
		"""

    def delete(self):
        """
		Docstring
		---
		description: Delete a user by username
		parameters:
    	- $ref: '#/components/parameters/username'
		responses:
			'204':
				description: The user has been deleted
			'404':
				description: The user was not found
		"""
        pass


class UserReviewCollection(Resource):
    def get(self):
        """
		Docstring
		---
		description: Get the list of a user's reviews by username
		parameters:
    	- $ref: '#/components/parameters/username'
		responses:
			'200':
			description: List of reviews
			content:
				application/json:
					example:
					- rating: 3
					  comment: The movie is ok
					  date: 20210322
					- rating: 5
					  comment: The movie is great
					  date: 20210323
		"""
        pass


# Movie -----------
class MovieCollection(Resource):

    def get(self):
        """
		Docstring
		---
		description: Get the list of manage movies
		responses:
			'200':
				description: List of movies
				content:
					application/json:
						example:
						- title: test-movie-1
						  length: 172
						- title: test-movie-2
						  director: Nolan
						  length: 168
						  release_date: 20180627
		"""
        pass

    def post(self):
        """
		Docstring
		---
		description: Create a new movie
		responses:
			'201':
				description: The movie was created successfully
				headers:
					Location:
						description: URI of the new movie
						schema:
							type: string
			'400':
				description: title, director must be string, length must be a number and releas_date must be a number with YYYYMMDD format
			'409':
				description: Movie already exists
			'415':
				description: Request content type must be JSON
		requestBody:
			description: JSON document that contains basic data for a new movie
			content:
				application/json:
					schema:
						$ref: '#/components/schemas/Movie'
					example:
						title: new-test-user-1
						director: villeneuve
		"""
        pass


class MovieItem(Resource):
    def get(self):
        """
		Docstring
		---
		description: Get details of one movie by title
		parameters:
    	- $ref: '#/components/parameters/movie_title'
		responses:
			'200':
				description: Data of single movie
				content:
				application/json:
					examples:
						movie-example:
						description: A movie that has been created
						value:
							title: test-movie-1
							length: 172
			'404':
				description: The movie was not found
		"""
        pass

    def put(self):
        """
		Docstring
		---
		description: Update a movie by title
		parameters:
    	- $ref: '#/components/parameters/movie_title'
		responses:
			'204':
				description: The movie has been deleted
			'404':
				description: The movie was not found
		"""
        pass

    def delete(self):
        """
		Docstring
		---
		description: Delete a movie by title
		parameters:
    	- $ref: '#/components/parameters/movie_title'
		responses:
			'204':
				description: The movie has been deleted
			'404':
				description: The movie was not found
		"""
        pass


class MovieReviewCollection(Resource):
    def get(self):
        """
		Docstring
		---
		description: Get the list of a movie's reviews by title
		 parameters:
    	- $ref: '#/components/parameters/movie_title'
		responses:
			'200':
			description: List of reviews
			content:
				application/json:
					example:
					- rating: 3
					  comment: The movie is ok
					  date: 20210322
					- rating: 5
					  comment: The movie is great
					  date: 20210323
		"""
        pass


class MovieReviewItem(Resource):
    def get(self):
        """
        Docstring
        ---
        description: Get details of one review
        parameters:
		- $ref: '#/components/parameters/movie_title'
		- $ref: '#/components/parameters/review_comment'
        responses:
            '200':
                description: Data of single review by movie title and review comment
                content:
                application/json:
                    examples:
                        movie-example:
                        description: A review that has been created
                        value:
                            rating: 3
							comment: The movie is ok
							date: 20210322
            '404':
                description: The review was not found
        """
        pass

    def put(self):
        """
        Docstring
        ---
        description: Update a review by movie title and comment
        parameters:
		- $ref: '#/components/parameters/movie_title'
		- $ref: '#/components/parameters/review_comment'
        responses:
            '204':
                description: The review has been deleted
            '404':
                description: The review was not found
        """
        pass

    def delete(self):
        """
        Docstring
        ---
        description: Delete a review by movie title and comment
        parameters:
		- $ref: '#/components/parameters/movie_title'
		- $ref: '#/components/parameters/review_comment'
        responses:
            '204':
                description: The review has been deleted
            '404':
                description: The review was not found
        """
        pass


# Category -----------
class CategoryCollection(Resource):
    def get(self):
        """
        Docstring
        ---
        description: Get the list of manage categories
        responses:
            '200':
                description: List of categories
                content:
                    application/json:
                        example:
                        - title: test-category-1
              			- title: test-category-2
        """
        pass

    def post(self):
        """
        Docstring
        ---
        description: Create a new movie
        responses:
            '201':
                description: The category was created successfully
                headers:
                    Location:
                        description: URI of the new category
                        schema:
                            type: string
            '400':
                description: title must be string
            '409':
                description: Category already exists
            '415':
                description: Request content type must be JSON
        requestBody:
            description: JSON document that contains basic data for a new movie
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/Category'
                    example:
                        title: new-test-user-1
                        director: villeneuve
        """
        pass


class CategoryItem(Resource):
    def get(self):
        """
        Docstring
        ---
        description: Get details of one category
        parameters:
    	- $ref: '#/components/parameters/category_title'
        responses:
            '200':
                description: Data of single category
                content:
                application/json:
                    examples:
                        movie-example:
                        description: A movie that has been created
                        value:
                            title: test-category-1
            '404':
                description: The category was not found
        """
        pass

    def put(self):
        """
        Docstring
        ---
        description: Update a category by title
        parameters:
    	- $ref: '#/components/parameters/category_title'
        responses:
            '204':
                description: The category has been deleted
            '404':
                description: The category was not found
        """
        pass

    def delete(self):
        """
        Docstring
        ---
        description: Delete a category by title
        parameters:
    	- $ref: '#/components/parameters/category_title'
        responses:
            '204':
                description: The category has been deleted
            '404':
                description: The category was not found
        """
        pass
