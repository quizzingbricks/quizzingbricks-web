      var addTokenOnBoard = function( x, y, player )
        {
            dojo.place( this.format_block( 'jstpl_token', {
                x_y: x+'_'+y,
                color: this.gamedatas.players[ player ].color
            } ) , 'tokens' );
            
            this.placeOnObject( 'token_'+x+'_'+y, 'overall_player_board_'+player );
            this.slideToObject( 'token_'+x+'_'+y, 'square_'+x+'_'+y ).play();
            console.log("log test")
        }
