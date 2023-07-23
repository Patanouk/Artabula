docker container run \
      -d \
      --name wikimedia-mysql \
      -e MYSQL_USER=jean \
      -e MYSQL_PASSWORD=jean \
      -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
      -e MYSQL_DATABASE=wikimedia \
      -p 3306:3306 \
      -v "${PWD}"/monuments_db.sql:/docker-entrypoint-initdb.d/monuments_db.sql \
      mysql:8.0.33