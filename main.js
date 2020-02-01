var app = new Vue({
	el: '#root',
	data: {
		appName: 'Flask CRUD',
		things: [],
	},
	methods: {
		api: function(){
            this.things = []
            var url = "http://127.0.0.1:5000/api"
            fetch(url).then(response => response.json()).then(json => {
                for (var i = 0; i <= json.results.length - 1; i++){
                    let thing = new Object()
                    thing.id = json.results[i].thing_id
                    thing.name = json.results[i].name
                    thing.desc = json.results[i].description
                    this.things.push(thing)
                }
            })
		}
    },
    mounted(){
        this.api()
    }
});