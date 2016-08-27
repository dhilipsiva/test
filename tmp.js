function rot13(str) {
	var i, position, num, str2 = "";
	for(i=0; i<str.length; i++){
		num = 0;
		position = str.charCodeAt(i);
		if (position >= 65 && position < 78) {
			num = 13;
		}
		else if (position >=78 && position <= 90){
			num = -13;
		}
		str2 += String.fromCharCode(position + num);
	}
	return str2;
}
rot13("SERR PBQR PNZC");
