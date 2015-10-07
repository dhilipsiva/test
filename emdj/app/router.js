import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('project', {path: '/project/:project_uuid'});
  this.route('file', {path: '/file/:file_uuid'});
});

export default Router;
