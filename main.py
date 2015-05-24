import tornado.ioloop
import tornado.web
import tornado.autoreload
import torndb

items = []

db = torndb.Connection("localhost",
	"tsukkomi", 
	"root",
	"12341234")

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html", items=items)
		for content in db.query("SELECT * FROM content"):
			item.add(content.text)

	def post(self):
		self.set_header("Content-Type", "text/plain")
		item = self.get_argument("content")
		r = db.insert('INSERT INTO content (text, ip) VALUES (%s, %s)', item, "255.255.255.255")
		self.redirect("/")

if __name__ == "__main__":
	application = tornado.web.Application([
		(r"/", MainHandler),
	], 
	debug=True)
	application.listen(1234)
	tornado.ioloop.IOLoop.instance().start()
