import falcon
import requests
import ffmpeg
import movieConvert

class MovieUpload(object):
    def on_post(self,req,resp):
        
        movieComvert.mainRoute()


app = falcon.API()
movie = MovieUpload()
app.add_route('/movie',movie)

