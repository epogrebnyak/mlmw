publish:
   npx prettier markdown --write
   mdbook build
   ghp-import -pn book