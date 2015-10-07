import Ember from 'ember';

export default Ember.Mixin.create({
  isChildrenLoaded: false,
  loadChildren: function(){
    if(this.get("isChildrenLoaded")){
      return;
    }
    var children = this.get("children"), uuid = this.get("uuid"), self = this;
    this.store.query(children, {uuid: uuid}).then(function(children){
      self.set("isChildrenLoaded", true)
    })
  }
});
