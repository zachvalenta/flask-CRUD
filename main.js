var app = new Vue({
	el: '#root',
	data: {
        appName: 'Flask CRUD',
        query: '',
		things: [],
	},
	methods: {
		api: function(){
            this.query = ""
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
        },
        search: function(){
            if(this.query){
                this.things.length = 0;
                console.log(this.query)
                var url = "http://127.0.0.1:5000/search?query=" + this.query
                console.log(url)
                fetch(url)
                .then(response => response.json())
                .then(json => {
                    for (var i = 0; i <= json.results.length - 1; i++){
                        let thing = new Object();
                        thing.id = json.results[i].thing_id
                        thing.name = json.results[i].name
                        thing.desc = json.results[i].description
                        this.things.push(thing)
                    }
                })
            }
            else{
                alert("enter search query")
            }
        }
    },
    mounted(){
        this.api()
    }
});