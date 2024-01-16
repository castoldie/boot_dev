FROM debian:stable-slim
COPY boot_dev /bin/boot_dev
ENV GOOS=linux
ENV GOARCH=amd64
CMD ["/bin/boot_dev"]
