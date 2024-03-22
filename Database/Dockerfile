FROM mysql

ENV MYSQL_ROOT_PASSWORD=apiuserpass

COPY ./Create /docker-entrypoint-initdb.d

EXPOSE 3306 