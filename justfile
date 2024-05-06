brush:
   npx prettier markdown --write

build:
   bin/mdbook clean
   bin/mdbook build

publish:
   ghp-import -pn book/html --cname=trics.me
