FROM debian:stable-slim
COPY main.go /bin/main.go
CMD ["/bin/main.go"]
