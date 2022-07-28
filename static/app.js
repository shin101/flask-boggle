class BoggleGame{

    // STUCK ON WHAT SHOULD GO INSIDE CONSTRUCTOR....
    constructor() {
        $('.submit-form').on('submit', this.handleSubmit);
        this.score = 0;
    }

    async handleSubmit(e){
        e.preventDefault();
        
        let input = $('input').val(); 
        let res = await axios.get('/check-word', { params: { word: input } });

        console.log(res.data)
        let result = res.data.result;
        $('.result').text(result)

    };

    // HOW DO I GET TIMER TO SHOW??? 
    setTimer(){
        let timeleft= 50;
        let timer = setInterval(()=>{
            if(timeleft=0){
                clearInterval(timer);
            }
            timeleft -=1;
        })

    }
}

let game = new BoggleGame();
// this refers to entire document when it is outside of class scope
// $('.submit-form').on('submit', (e) => game.handleSubmit);
