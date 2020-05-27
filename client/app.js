$(function(){
  var url = "http://127.0.0.1:5000/load_player_names";
  $.get(url, function(data,status) {
    $("#my_input").autocomplete({
      source: function(request, response) {
        var results = $.ui.autocomplete.filter(data.all_players, request.term);
        response(results.slice(0, 10));
      }
    });
  });
});

function onClickedSimilarPlayers(){
  // get elements by ID
  $("#similar_player_table").remove();

  // create a table
  create_table();

  var player = document.getElementById('my_input').value;
  var url = "http://127.0.0.1:5000/similar_players";
  console.log(player)
  // using jquery to POST
  $.post(url, {
    player: player,
    num_player: 30
  }, function (json_data,status){
    data = json_data.similar_players;
    // console.log(data);
    // console.log(status);
    var player_data = '';
    $.each(data, function(key,value){
      player_data += '<tr>';
      player_data += '<td>'+value[0]+'</td>';
      player_data += '<td>'+value[1]+'</td>';
      player_data += '<td>'+value[2]+'</td>';
      player_data += '<td>'+value[3]+'</td>';
      player_data += '<td>'+value[4] +" %"+'</td>';
      player_data += '</tr>';
    });
    $("#similar_player_table").append(player_data);
  });
}

function create_table(){
  var tableDiv = document.getElementById('TABLE');
  var table = document.createElement('TABLE');
  table.setAttribute("id","similar_player_table");

  var columns = ['Name','Overall','Age','Position','Similarity Score'];
  var row = document.createElement('TR');
  for (var i=0; i<5; i++){
    var th = document.createElement('TH');
    th.innerHTML = columns[i];
    row.appendChild(th);
  }
  table.appendChild(row)
  tableDiv.appendChild(table);
}

function clearTable(){
  $("#similar_player_table").remove();
}

// window.onload = onPageLoad;
