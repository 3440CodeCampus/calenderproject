function deleteCalenderEntry(event){
  var $event = $(event)
  $event.parent().remove()
  var id = $event.data('id')

  $.ajax({
    url:'entry/delete/' + id,
    method:'DELETE',
    beforeSend:function(xhr){
      xhr.setRequestHeader('X-CSRFToken', csrf_token)
    }
  })
}
