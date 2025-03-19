# File Upload

## Limits

Our platform imposes limits on incoming & uploaded files in different ways.

### Front-end

There's a size limit on file drop-down component that can be adjusted by modifying `maxUploadedFileSize` value (number in MB) in the JS config (usually in the root of deployed front-end in `config.js`).

### Back-end

There are two config values seemingly responsible for handling file size limits on back-end imposed by Akka:

1. `akka.http.server.parsing.max-content-length`.
2. `akka.http.routing.decode-max-size`.

It's best to update both of those to the same value. Those values are likely present in the `conf/application.conf` file in your back-end deployment.

### Other infrastructure

Postal mail server and our routing infrastructure may also impose additional limits on file sizes.

!!! warning "TODO: document infra part in more detail"
