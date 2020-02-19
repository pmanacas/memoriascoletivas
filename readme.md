# Memórias Coletivas - Cova do Vapor

Este projeto, iniciado em Junho de 2013, agrupa  fotografias que representam a história e a evolução da comunidade da Cova do Vapor. O site serve de repositório digital para as [fotografias](http://www.memoriascoletivas.pt/galeria) cedidas pelos membros da comunidade.


**Link para o site:**
[http://www.memoriascoletivas.pt/](http://www.memoriascoletivas.pt/)
ou [http://memoriascoletivas.appspot.com/](http://memoriascoletivas.appspot.com/)

## Informação técnica
### Server side:
 - Python 2.7 app hosted on [Google AppEngine Standard Environment](https://cloud.google.com/appengine/docs/standard/python/runtime)
 - Google NoSQL Datastore (stores all the metadata for the image files)
 - Jinja 2 templates
 - the actual image files are hosted on flickr.com


### Front-end:
 - HTML, CSS, Javascript
 - Bootstrap 3.0
 - Jquery
 - [slimbox2](https://www.digitalia.be/software/slimbox2/) (for image zoom popout)
 - [lazyload](https://appelsiini.net/projects/lazyload/v1/) (for loading images only when users scrolls to them)
 - [jQCloud](https://github.com/mistic100/jQCloud) (for displaying the [nice tag clouds](http://www.memoriascoletivas.pt/tags))





