using System;
using Gtk;

namespace JamRin
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Application.Init ();
			MainWindow win = new MainWindow ();
			win.Show ();
			var browser =  new 
			Application.Run ();
		}
	}
}
