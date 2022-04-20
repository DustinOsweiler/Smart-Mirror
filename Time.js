const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://world-clock.p.rapidapi.com/json/est/now",
	"method": "GET",
	"headers": {
		"X-RapidAPI-Host": "world-clock.p.rapidapi.com",
		"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
});