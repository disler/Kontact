/**
* Client side utility class
*/
class Util
{
    /**
     * Determines if a variable is strictly an object, not array, not null
     * @param {any} item - variable to test if object
     */
    isObject(item) {
        return (item && typeof item === 'object' && !Array.isArray(item));
    }

    /**
     * Deep merge two objects. Note circular references will result in infinite recurision
     * @param {object} target - target to merge objects into
     * @param {object} ...sources - sources to merge, the last being the overwritting
     * @returns {object} object merged
     */
    DeepMerge(target, ...sources) 
    {
        if (!sources.length) 
            return target;
        const source = sources.shift();

        if (this.isObject(target) && this.isObject(source)) 
        {
            for (const key in source) 
            {
                if (this.isObject(source[key])) 
                {
                    if (!target[key]) 
                        Object.assign(target, { [key]: {} });
                    this.DeepMerge(target[key], source[key]);
                } 
                else 
                {
                    Object.assign(target, { [key]: source[key] });
                }
            }
        }

        return this.DeepMerge(target, ...sources);
    }
}

module.exports = new Util();