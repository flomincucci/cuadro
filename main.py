import argparse
import glib
import gtk
import webkit


class ReloadView:
    def __init__(self, width=1920, height=1080, ttr=10):
        window = gtk.Window()
        window.connect('delete-event', gtk.main_quit)

        self.view = webkit.WebView()
        self.view.load_uri(
            'https://unsplash.it/%(width)s/%(height)s/?random' % locals())
        glib.timeout_add_seconds(ttr, self.reload)

        window.add(self.view)
        window.fullscreen()
        window.show_all()

    def reload(self):
        self.view.reload()
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--width", dest="width",
                      help="width of the image",
                      default=1920)
    parser.add_argument("-hh", "--height", dest="height",
                      help="height of the image",
                      default=1080)
    parser.add_argument("-t", "--time", dest="ttr",
                      help="time to refresh the image",
                      default=10)
    args = parser.parse_args()

    ReloadView(width=args.width, height=args.height,
               ttr=args.ttr)
    gtk.main()
