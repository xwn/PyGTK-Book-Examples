# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;
import gtk.glade;

# ... #

def delete_event( widget, data ):
	False;

def destroy( widget, data = None ):
	gtk.main_quit();

def buttonClicked( widget, data = None ):
	widget.set_label( 'تم الضغط على الزر' );

# ... #

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

# ... #

window = builder.get_object( 'main_window' );
button = builder.get_object( 'hello_world_button' );

# ... #

window.connect( 'delete_event', delete_event );
window.connect( 'destroy', destroy );

button.connect( 'clicked', buttonClicked );

# ... #

window.show();
button.show();

gtk.main();
