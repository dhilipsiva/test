import Ember from 'ember';
import ChildrenLoaderMixin from '../../../mixins/children-loader';
import { module, test } from 'qunit';

module('Unit | Mixin | children loader');

// Replace this with your real tests.
test('it works', function(assert) {
  var ChildrenLoaderObject = Ember.Object.extend(ChildrenLoaderMixin);
  var subject = ChildrenLoaderObject.create();
  assert.ok(subject);
});
