# api-employee

api para cadastro de usuarios
- Banco de dados:
    
    para iniciar o banco de dados necessário arquivo .env com a url de conexão contendo usuários e senha. A variavél deve ter o nome <b>DATABASE_URI</b>

    após configuração da .env, para criar as tabelas o arquivo database, dentro do diretorio database, precisará ser executado, ele apagará as atuais tabelas da database se houver e criará as novas tabelas.

- Requerimets:

    dentro do projeto contém o arquivo requeriments.txt, para instalar no ambiente que será executado a aplicação deve rodar o comando:
    
    `pip install -r requirements. txt`

    o pip já terá que estar instalado no ambiente.

- Testes:

    para rodar os testes, será necessário rodar o comando unittest:
        
    para todos os testes:
            
    `python3 -m  unittest`

    para um arquivo especifico:

    `python3 -m unittest test/arquivo_especifico.py`

- Swagger aplicacao:

          
        swagger: "2.0"

        info:
        description: "api para cadastro de funcionario"
        version: "1.0.0"
        title: "Swagger Employee"
        termsOfService: "http://swagger.io/terms/"
        contact:
            email: "apiteam@swagger.io"
        license:
            name: "Apache 2.0"
            url: "http://www.apache.org/licenses/LICENSE-2.0.html"
        host: "employee.swagger.io"
        basePath: "/"
        tags:
        - name: "employee"
        description: "Operations about employees"
        - name: "position"
        description: "Operations about positions"
        - name: "leader"
        description: "Operations about leaders"
        schemes:
        - "https"
        - "http"
        paths:

        /employee:
            post:
            tags:
            - "employee"
            summary: "Add a new employee to the database"
            description: ""
            operationId: "addEmployee"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - in: "body"
                name: "body"
                description: "employee object that needs to be added to the db"
                required: true
                schema:
                $ref: "#/definitions/Employee"
            responses:
                "201":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Employee"
                "400":
                description: "invalid input"
                "500":
                description: "internal server error"
            get:
            tags:
            - "employee"
            summary: "Find employees"
            description: "Multiple status values can be provided with comma separated strings"
            operationId: "findEmployee"
            produces:
            - "application/json"
            parameters:
            - name: "registration"
                in: "query"
                description: "value registration employee"
                type: "number"
            - name: "name"
                in: "query"
                description: "name employee"
                type: "string"
            - name: "last_name"
                in: "query"
                description: "last name employee"
                type: "string"
            - name: "code_position"
                in: "query"
                description: "code about position"
                type: "number"
            - name: "salary"
                in: "query"
                description: "salary about employee"
                type: "number"
            - name: "status"
                in: "query"
                description: "status employee"
                type: "string"
                
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Employee"
                "404":
                description: "not found employee"
                "400":
                description: "invalid value"
                "500":
                description: "internal server error"
                
        /employee/{registration}:  
            put:
            tags:
            - "employee"
            summary: "Update an existing employee"
            description: "update info about employee"
            operationId: "updateEmployee"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - name: "registration"
                in: "path"
                description: "ID of employee to update"
                required: true
                type: "integer"
                format: "int64"
            - in: "body"
                name: "body"
                description: "employee object that needs to be update to the db"
                required: true
                schema:
                $ref: "#/definitions/Employee"
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Employee"
                "400":
                description: "invalid request"
                "404":
                description: "employee not found"
                "500":
                description: "internal server error"
            delete:
            tags:
            - "employee"
            summary: "Delete employee order by registration"
            description: "For delete a employee put a valid registration"
            operationId: "employeeDelete"
            produces:
            - "application/json"
            parameters:
            - name: "registration"
                in: "path"
                description: "registration of the employee that needs to be deleted"
                required: true
                type: "number"
            responses:
                "200":
                description: "sucessful delete employee"
                "400":
                description: "invalid registration employee"
                "500":
                description: "internal server error"
                
        /position:
            post:
            tags:
            - "position"
            summary: "Add a new position to the database"
            description: ""
            operationId: "addPosition"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - in: "body"
                name: "body"
                description: "position object that needs to be added to the db"
                required: true
                schema:
                $ref: "#/definitions/Position"
            responses:
                "201":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Position"
                "400":
                description: "invalid input"
                "500":
                description: "internal server error"
            get:
            tags:
            - "position"
            summary: "Find position"
            description: "Multiple status values can be provided with comma separated strings"
            operationId: "findPosition"
            produces:
            - "application/json"
            parameters:
            - name: "title"
                in: "query"
                description: "title of position"
                type: "string"
            - name: "code_team"
                in: "query"
                description: "code team of position"
                type: "string"
            - name: "status"
                in: "query"
                description: "status of position"
                type: "string"
                
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Position"
                "404":
                description: "not found position"
                "400":
                description: "invalid value"
                "500":
                description: "internal server error"
                
        /position/{id}:  
            put:
            tags:
            - "position"
            summary: "Update an existing position"
            description: "update info about position"
            operationId: "updatePosition"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - name: "id"
                in: "path"
                description: "id of position to update"
                required: true
                type: "number"
            - in: "body"
                name: "body"
                description: "position object that needs to be update to the db"
                required: true
                schema:
                $ref: "#/definitions/Position"
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Position"
                "400":
                description: "invalid request"
                "404":
                description: "position not found"
                "500":
                description: "internal server error"

        /leader:
            post:
            tags:
            - "leader"
            summary: "Add a new leader to the database"
            description: ""
            operationId: "addLeader"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - in: "body"
                name: "body"
                description: "leader object that needs to be added to the db"
                required: true
                schema:
                $ref: "#/definitions/Leader"
            responses:
                "201":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Leader"
                "400":
                description: "invalid input"
                "500":
                description: "internal server error"
            get:
            tags:
            - "leader"
            summary: "Find position"
            description: "Multiple status values can be provided with comma separated strings"
            operationId: "findLeader"
            produces:
            - "application/json"
            parameters:
            - name: "code_employee"
                in: "query"
                description: "code of employee"
                type: "number"
            - name: "code_team"
                in: "query"
                description: "code team of position"
                type: "number"
            - name: "code_position"
                in: "query"
                description: "status of position"
                type: "string"
                
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Position"
                "404":
                description: "not found leader"
                "400":
                description: "invalid value"
                "500":
                description: "internal server error"
                
        /leader/{id}:  
            put:
            tags:
            - "leader"
            summary: "Update an existing leader"
            description: "update info about leader"
            operationId: "updateLeader"
            consumes:
            - "application/json"
            produces:
            - "application/json"
            parameters:
            - name: "id"
                in: "path"
                description: "id of leader to update"
                required: true
                type: "number"
            - in: "body"
                name: "body"
                description: "leader object that needs to be update to the db"
                required: true
                schema:
                $ref: "#/definitions/Leader"
            responses:
                "200":
                description: "successful operation"
                schema:
                    type: "array"
                    items:
                    $ref: "#/definitions/Leader"
                "400":
                description: "invalid request"
                "404":
                description: "leader not found"
                "500":
                description: "internal server error"

        definitions:
        Employee:
            type: "object"
            required:
            - "name"
            - "last_name"
            - "code_position"
            - "salary"
            - "password"
            - "status"
            properties:
            name:
                type: "string"
                example: "Josimar"
            last_name:
                type: "string"
                example: "Rachetti"
            code_position:
                type: "number"
                example: 100
            salary:
                type: "number"
                example: 1500.00
            password:
                type: "string"
                example: "32323rf##"
            status:
                type: "string"
                example: "ABERTA"
        Position:
            type: "object"
            required:
            - "title"
            - "description"
            - "code_team"
            - "status"
            properties:
            title:
                type: "string"
                example: "analista desenvolvimento"
            description:
                type: "string"
                example: "construir apis"
            code_team:
                type: "string"
                example: "AA22"
            status:
                type: "string"
                example: "ABERTA"
        Leader:
            type: "object"
            required:
            - "code_employee"
            - "code_position"
            - "code_team"
            properties:
            code_employee:
                type: "number"
                example: 1002
            code_position:
                type: "number"
                example: 100
            code_team:
                type: "string"
                example: "AA22"

        externalDocs:
        description: "Find out more about Swagger"
        url: "http://swagger.io"