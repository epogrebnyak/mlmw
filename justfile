brush:
   npx prettier markdown --write

build:
   bin/mdbook clean
   bin/mdbook build

publish:
   ghp-import -pn book --cname=trics.me
