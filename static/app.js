let timer = 5; 

class BoggleGame{

    constructor() {
        $('.submit-form').on('submit', this.handleSubmit.bind(this));
        this.score = 0;
        $('#cur_score').text(this.score);
        $('#timer').text(timer);
        this.setTimer();
        this.words = new Set();
        this.highscore = 0;
        $('#highscore').text(0);
    }

    async handleSubmit(e){
        e.preventDefault();
        
        let input = $('input').val(); 
        let res = await axios.get('/check-word', { params: { word: input } });

        let result = res.data.result;
        $('.result').html(result);

        if(this.words.has(input)){
            return $('.result').text('cannot choose the same word again.')
        }

        if(result==='ok'){
            this.score += input.length
            $('#cur_score').text(this.score)
            this.words.add(input)
            $('.words_list').append('<li>' + input + '</li>')
        } 

    };

    setTimer(){
        let timeLeft=timer;
        let printCount = setInterval(()=>{
            timeLeft--;
            document.getElementById("timer").innerText = timeLeft;
            if(!timeLeft){
                alert('Game Over');
                clearInterval(printCount);
                this.scoreGame();
            }
          }, 1000);
    }

    async scoreGame(){
        $(".submit-form", this.board).hide();
        let res = await axios.post('/nplays');
        if(this.score>this.highscore){
            this.highscore = this.score;
            return $('#highscore').text(this.highscore)
            

        }
    }
}




let game = new BoggleGame();
// this refers to entire document when it is outside of class scope
// $('.submit-form').on('submit', (e) => game.handleSubmit);
