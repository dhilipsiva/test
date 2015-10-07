import Ember from 'ember';
import RouteChildrenMixin from '../../../mixins/route-children';
import { module, test } from 'qunit';

module('Unit | Mixin | route children');

// Replace this with your real tests.
test('it works', function(assert) {
  var RouteChildrenObject = Ember.Object.extend(RouteChildrenMixin);
  var subject = RouteChildrenObject.create();
  assert.ok(subject);
});
