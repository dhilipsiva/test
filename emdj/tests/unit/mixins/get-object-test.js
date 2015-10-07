import Ember from 'ember';
import GetObjectMixin from '../../../mixins/get-object';
import { module, test } from 'qunit';

module('Unit | Mixin | get object');

// Replace this with your real tests.
test('it works', function(assert) {
  var GetObjectObject = Ember.Object.extend(GetObjectMixin);
  var subject = GetObjectObject.create();
  assert.ok(subject);
});
