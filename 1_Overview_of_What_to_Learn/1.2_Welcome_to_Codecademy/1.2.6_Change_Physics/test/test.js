console.log = function () { };
const assert = require('chai').assert;
const fs = require('fs');
const Structured = require('structured');

const code = fs.readFileSync('index.js', 'utf8');

describe('', function () {
    it('', function () {
        let structure = function () {
            friction = $val
        };

        let varCallbacks = [
            function ($val) {
                if ($val.value === 0.85) {
                    return { failure: 'Change your code so `friction` equals something other than `0.85`.' };
                }
                return true;
            }
        ];

        let isMatch = Structured.match(code, structure, { varCallbacks: varCallbacks });
        let failureMessage = varCallbacks.failure || 'Did you set `friction` equal to a number other than `0.85`?';
        assert.isOk(isMatch, failureMessage);
    });
});
