# docker-tbc_shacl_cleaner

I use TopBraid Composer to generate SHACL shapes from an existing ontology. The generated SHACL shapes are missing a few things such as `sh:targetClass`. This docker script adds these post-processing cleanup tasks to produce a cleaned SHACL shape file ready to be used. 

## Build image

```
docker build --no-cache -t tbc-shacl-cleaner .
```

## Run the image

```
docker run --rm --name tbc-shacl-cleaner -e SHACL_FILE="test.shape.ttl" -v ${PWD}:/home/input tbc-shacl-cleaner
```


## Run from Docker Hub

```
docker run --rm --name tbc-shacl-cleaner -e SHACL_FILE="test.shape.ttl" -v ${PWD}:/home/input edmondchuc/tbc-shacl-cleaner
```